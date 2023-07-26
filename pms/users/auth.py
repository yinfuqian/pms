# -*- coding: utf-8 -*-
# @Time : 2023/6/27 16:12
# @Author : yinfuqian
# @File : auth.py
# @Project : pms
import datetime
from django.utils.translation import  gettext_lazy as _
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from rest_framework import HTTP_HEADER_ENCODING


# 获取请求头信息
def get_authorization_header(request):
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, type('')):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


# 自定义认证方式，这个是后面要添加到设置文件的
class ExpiringTokenAuthentication(BaseAuthentication):
    model = Token

    def authenticate(self, request):
        auth = get_authorization_header(request)
        if not auth:
            return None
        try:
            token = auth.decode()
        except UnicodeError:
            msg = _("无效的Token， Token头不应包含无效字符")
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        # 尝试从缓存获取用户信息（设置中配置了缓存的可以添加，不加也不影响正常功能）
        token_cache = 'token_' + key
        cache_user = cache.get(token_cache)
        if cache_user:
            return cache_user, cache_user  # 这里需要返回一个列表或元组，原因不详
        # 缓存获取到此为止

        # 下面开始获取请求信息进行验证
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed("认证失败")

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("用户被禁用")

        # Token有效期时间判断（注意时间时区问题）
        # 我在设置里面设置了时区 USE_TZ = False，如果使用utc这里需要改变。
        if (datetime.datetime.now() - token.created) > datetime.timedelta(hours=0.1 * 1):
            raise exceptions.AuthenticationFailed('认证信息已过期')

        # 加入缓存增加查询速度，下面和上面是配套的，上面没有从缓存中读取，这里就不用保存到缓存中了
        if token:
            token_cache = 'token_' + key
            cache.set(token_cache, token.user, 600)

        # 返回用户信息
        return token.user, token

    def authenticate_header(self, request):
        return 'Token'