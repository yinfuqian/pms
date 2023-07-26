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
    path('create', views.create_product),
    # path('delete/<int:product_id>', views.delete_product),
    # path('update/<int:product_id>', views.update_product),
]