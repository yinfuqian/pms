from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class PmsOperationLogs(models.Model):
    user = models.CharField(max_length=50, verbose_name="操作用户", null=False, unique=False)
    timestamp = models.CharField(max_length=50, verbose_name="操作时间", default="")
    content = models.TextField(verbose_name="操作内容")
    operation_type = models.CharField(max_length=50, verbose_name="操作类型")
    project_name = models.CharField(max_length=50, verbose_name="项目名称", default="")
    file_name = models.CharField(max_length=50, verbose_name="文件名称", default="")

    class Meta:
        db_table = 'pms_operations_logs'
        verbose_name = '操作日志'
        verbose_name_plural = verbose_name
