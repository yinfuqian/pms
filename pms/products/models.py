# Create your models here.
# Create your models here.

from django.db import models


class PmsProductsList(models.Model):
    product_name = models.CharField(max_length=50, verbose_name="产品名称", null=False, unique=False, default="")
    product_version = models.CharField(max_length=50, verbose_name="部署版本", null=False, unique=False,
                                       default="v1.0.0")
    product_install_method = models.CharField(max_length=50, verbose_name="部署方式", null=True, unique=False,
                                              default="未知")
    product_notes = models.CharField(max_length=50, verbose_name="产品备注", null=True, unique=False, default="无")
    class Meta:
        db_table = 'pms_products_list'
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name
