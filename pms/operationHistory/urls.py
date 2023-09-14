# -*- coding: utf-8 -*-
# @Time : 2023/9/12 10:06
# @Author : yinfuqian
# @File : urls.py
# @Project : Project
from django.urls import path

from . import views

urlpatterns = [
    #path('list', views.operation_history_list),
    path('record_user_operation', views.record_user_operation),
    path('list', views.operations_list),
    path('search', views.operations_search)
]