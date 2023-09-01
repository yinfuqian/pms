# -*- coding: utf-8 -*-
# @Time : 2023/7/26 10:14
# @Author : yinfuqian
# @File : urls.py
# @Project : Project
from django.urls import path

from . import views

urlpatterns = [
    path('list', views.projects_list),
    path('search', views.search_project),
    path('create', views.create_project),
    path('delete/<int:project_id>', views.delete_project),
    path('update/<int:project_id>', views.update_project),
]