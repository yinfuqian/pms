# -*- coding: utf-8 -*-
# @Time : 2023/8/29 14:32
# @Author : yinfuqian
# @File : urls.py
# @Project : Project
from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload_file, name='upload_file'),
    path('list', views.list_file, name='list_file'),
    path('download', views.download_file, name='download_file'),
]