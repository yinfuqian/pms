# -*- coding: utf-8 -*-
# @Time : 2023/6/27 15:36
# @Author : yinfuqian
# @File : urls.py
# @Project : pms
from django.urls import path, include

urlpatterns = [
    path('user/', include('users.urls')),
    path('products/', include('products.urls')),
    path('mainProjects/', include('mainProjects.urls')),
    path('file/', include('upload.urls'))
]
