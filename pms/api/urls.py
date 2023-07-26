# -*- coding: utf-8 -*-
# @Time : 2023/6/27 15:36
# @Author : yinfuqian
# @File : urls.py
# @Project : pms
from django.urls import path, include
from users import views

urlpatterns = [
    path('login/', views.login),
    path('check_token/', views.check_token),
    path('get_user/', views.get_user),
    path('search_user/', views.search_user),
    path('create_user', views.create_user),
    path('update_user/<int:user_id>', views.update_user),
    path('delete_user/<int:user_id>', views.delete_user),
    path('products/', include('products.urls')),
    path('mainProjects/', include('mainProjects.urls')),
]
