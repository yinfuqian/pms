# test0 /123456
# Create your views here.
from django.contrib import auth
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from .models import PmsUserProfile


@api_view(['POST'])
# 登陆
def login(request):
    receive = request.data
    username = receive.get('username')
    password = receive.get('password')

    #print(receive)
    user = auth.authenticate(username=username, password=password)
    #print(username, password)
    if not user:
        return JsonResponse({"code": 1, "msg": "用户密码不匹配", "token": "null"})
    """校验通过，删除token"""
    old_token = Token.objects.filter(user=user)
    old_token.delete()
    """创建新token"""
    token = Token.objects.create(user=user)
    return JsonResponse({"code": 0, "msg": "用户密码匹配", "username": user.username, "token": token.key})


# token检查
def check_token(request):
    receive = request.data
    print(receive)

    if request.user.is_authenticated:  # 验证token是否正确
        print("token check success")
        return JsonResponse({"msg": "验证通过"})
    else:
        print("token check failed")
        return JsonResponse({"msg": "验证失败"})


# 创建用户
def create_user(request):
    reversed = request.POST
    username = reversed.get('username')
    password = reversed.get('password') or 'zhuiyi@666'
    usernicname = reversed.get('usernicname')
    userjob = reversed.get('userjob')
    userbase = reversed.get('userbase')
    userworknum = reversed.get('userworknum')
    useremail = reversed.get('useremail')
    userphonenum = reversed.get('userphonenum')
    if reversed.get('usernicname'):
        usernicname = PmsUserProfile._meta.get_field('usernicname').get_default()
    try:
        # 检查用户是否已经存在
        if PmsUserProfile.objects.filter(username=username).exists():
            return JsonResponse({"code": 2, "msg": "用户已存在"})
        # 创建用户
        user = PmsUserProfile.objects.create_user(username=username, password=password, usernicname=usernicname or None,
                                                  userjob=userjob, userbase=userbase, userworknum=userworknum,
                                                  useremail=useremail, userphonenum=userphonenum)
        return JsonResponse({"code": 0, "msg": "用户创建成功"})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1, "msg": "用户创建失败"})


@api_view(['GET'])
# 根据条件查询用户
def search_user(request):
    username = request.GET.get('username')
    try:
        user_list = []
        user = PmsUserProfile.objects.get(username=username)
        user_list.append({
            "id": user.id,
            "code": 0,
            "username": user.username,
            "password": user.password,
            "usernicname": user.usernicname,
            "userjob": user.userjob,
            "userbase": user.userbase,
            "userworknum": user.userworknum,
            "useremail": user.useremail,
            "userphonenum": user.userphonenum})
        return JsonResponse({"code": 0, "msg": "查询用户成功", "users": user_list})
    except Exception as e:
        return JsonResponse({
            'message': '用户不存在',
            'code': '1'
        }, status=404)


# 查询所有PM
def get_pm(request):
    users = PmsUserProfile.objects.filter(userjob="PM")
    user_list = []
    for user in users:
        user_list.append({
            "id": user.id,
            "code": 0,
            "username": user.username,
            "usernicname": user.usernicname,
            "userjob": user.userjob,
            "userbase": user.userbase,
            "userworknum": user.userworknum,
            "useremail": user.useremail,
            "userphonenum": user.userphonenum})
    return JsonResponse({"code": 0, "msg": "获取所有项目经理成功", "users": user_list})


# 查询所有TM
def get_tm(request):
    users = PmsUserProfile.objects.filter(userjob="技术经理")
    user_list = []
    for user in users:
        user_list.append({
            "id": user.id,
            "code": 0,
            "username": user.username,
            "usernicname": user.usernicname,
            "userjob": user.userjob,
            "userbase": user.userbase,
            "userworknum": user.userworknum,
            "useremail": user.useremail,
            "userphonenum": user.userphonenum})
    return JsonResponse({"code": 0, "msg": "获取所有技术经理成功", "users": user_list})


# 查询所有用户
def get_user(request):
    users = PmsUserProfile.objects.all()
    page_num = request.GET.get('pageNum')
    page_size = request.GET.get('pageSize')
    user_list = []
    if page_num and page_size:  # 判断是否传递了页码参数
        start = (int(page_num) - 1) * int(page_size)
        end = start + int(page_size)
        page_users = users[start:end]
        count = users.count()
        for user in page_users:
            user_list.append({
                "id": user.id,
                "code": 0,
                "username": user.username,
                "usernicname": user.usernicname,
                "userjob": user.userjob,
                "userbase": user.userbase,
                "userworknum": user.userworknum,
                "useremail": user.useremail,
                "userphonenum": user.userphonenum})
        data = {
            'count': count,
        }
        return JsonResponse({"code": 0, "msg": "获取所有用户成功", "users": user_list, "pagination": data})
    else:
        for user in users:
            user_list.append({
                "id": user.id,
                "code": 0,
                "username": user.username,
                "usernicname": user.usernicname,
                "userjob": user.userjob,
                "userbase": user.userbase,
                "userworknum": user.userworknum,
                "useremail": user.useremail,
                "userphonenum": user.userphonenum
            })

        return JsonResponse({"code": 0, "msg": "获取所有用户成功", "users": user_list})



@api_view(['PUT'])
# 更新用户
def update_user(request, user_id):
    try:
        user = PmsUserProfile.objects.get(id=user_id)
    except PmsUserProfile.DoesNotExist:
        return JsonResponse({"code": 1, "msg": "用户不存在"})

    reversed = request.data
    username = reversed.get('username')
    password = reversed.get('password')
    usernicname = reversed.get('usernicname')
    userjob = reversed.get('userjob')
    userbase = reversed.get('userbase')
    userworknum = reversed.get('userworknum')
    useremail = reversed.get('useremail')
    userphonenum = reversed.get('userphonenum')
    if reversed.get('username'):
        user.username = username
    if reversed.get('password'):
        user.set_password(password)
    if reversed.get('usernicname'):
        user.usernicname = usernicname
    if reversed.get('userjob'):
        user.userjob = userjob
    if reversed.get('userbase'):
        user.userbase = userbase
    if reversed.get('userworknum'):
        user.userworknum = userworknum
    if reversed.get('userphonenum'):
        user.useremail = useremail
    if reversed.get('userphonenum'):
        user.userphonenum = userphonenum
    try:
        user.save()
        return JsonResponse({"code": 0, "msg": "用户更新成功"})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1, "msg": "用户更新失败"})

# 删除用户
@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = PmsUserProfile.objects.get(id=user_id)
    except PmsUserProfile.DoesNotExit:
        return JsonResponse({"code": 2, "msg": "用户不存在"})
    try:
        user.delete()
        return JsonResponse({"code": 0, "msg": "用户删除成功"})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1, "msg": "用户删除失败"})
