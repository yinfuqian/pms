# -*- coding: utf-8 -*-
# @Time : 2023/7/19 10:26
# @Author : yinfuqian
# @File : urls.py
# @Project : Project
from django.urls import path

from . import views

urlpatterns = [
    path('list', views.products_list),
    path('search', views.search_product),
    path('create', views.create_product),
    path('delete/<int:product_id>', views.delete_product),
    path('update/<int:product_id>', views.update_product),
]
