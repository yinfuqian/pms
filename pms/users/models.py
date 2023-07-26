# Create your models here.
import random

from django.contrib.auth.models import AbstractUser
from django.db import models

# BASE_CHOICE = (
#     ("cd", "成都"),
#     ("bj", "北京"),
#     ("zj", "深圳"),
#     ("sh", "上海"),
#     ("gz", "广州"),
#     ("nx", "宁夏"),
#     ("xa", "西安"),
#     ("patnership", "合作企业"),
# )


# 默认用户昵称,邮箱，电话
def get_default():
    random_num = random.randint(1000, 9999)
    random_num = str(random_num)

    default_name = "zhuiyi" + random_num
    return default_name


def default_worknum():
    random_num = random.randint(10000, 99999)
    random_num = str(random_num)
    return random_num


def default_email():
    random_num = random.randint(1000000000, 9999999999)
    random_num = str(random_num)
    email_addr = random_num + "@wezhuiyi.com"
    return email_addr

def default_phone():
    random_num = random.randint(10000000000, 99999999999)
    random_num = str(random_num)
    return random_num


class PmsUserProfile(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="用户姓名", null=False, unique=True, default="临时用户")
    is_super = models.CharField(max_length=50, verbose_name="是否管理员", null=False, unique=False, default="0")
    usernicname = models.CharField(max_length=50, verbose_name="昵称", null=True, unique=True, default=get_default)
    userjob = models.CharField(max_length=50, verbose_name="岗位", null=True, unique=False, default="技术经理")
    userbase = models.CharField(max_length=50, verbose_name="地区", null=True, unique=False, default="CD")
    userworknum = models.CharField(max_length=50, verbose_name="工号", null=True, unique=True, default=default_worknum)
    useremail = models.CharField(max_length=50, verbose_name="邮箱", null=True, unique=True,
                                 default=default_email)
    userphonenum = models.CharField(max_length=11, verbose_name="电话", null=True, unique=True, default=default_phone)
    class Meta:
        db_table = 'pms_user_controller'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.usernicname:
            return self.usernicname
        else:
            return self.username
