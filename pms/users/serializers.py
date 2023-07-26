# -*- coding: utf-8 -*-
# @Time : 2023/6/26 15:22
# @Author : yinfuqian
# @File : serializers.py
# @Project : pms
from rest_framework import serializers
from .models import PmsUserProfile

class UserLoginServializer(serializers.ModelSerializer):

    class Meta:
        mode = PmsUserProfile



