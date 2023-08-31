# Create your models here.
# Create your models here.

from django.db import models


class PmsMainProjectsList(models.Model):
    project_name = models.CharField(max_length=50, verbose_name="项目名称", null=False, unique=True, default="")
    project_base = models.CharField(max_length=50, verbose_name="北东区域&南区", null=False, unique=False,
                                    default="北东区")
    project_num = models.CharField(max_length=50, verbose_name="项目编号", null=True, unique=True, default="未知")
    project_owner = models.CharField(max_length=50, verbose_name="所属PM", null=True, unique=False, default="无")
    project_resident = models.CharField(max_length=50, verbose_name="驻场TM", null=True, unique=False, default="无")
    project_product = models.CharField(max_length=50, verbose_name="部署产品", null=True, unique=False, default="未知")
    project_update_time = models.CharField(max_length=50, verbose_name="更新日期", null=True, unique=False,
                                           default="无")
    project_update_user = models.CharField(max_length=50, verbose_name="操作人", null=True, unique=False, default="无")
    project_update_file = models.CharField(max_length=50, verbose_name="更新文档", null=True, unique=False,
                                           default="文件列表")
    project_ivc = models.CharField(max_length=50, verbose_name="IVC", null=True, unique=False, default="追一自研")
    project_db = models.CharField(max_length=50, verbose_name="数据库", null=True, unique=False, default="追一自研")
    project_middleware = models.CharField(max_length=50, verbose_name="中间件", null=True, unique=False,
                                          default="追一自研")

    class Meta:
        db_table = 'pms_main_projects_list'
        verbose_name = '主线项目信息'
        verbose_name_plural = verbose_name














