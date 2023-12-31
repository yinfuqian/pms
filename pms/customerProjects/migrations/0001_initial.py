# Generated by Django 4.2.2 on 2023-09-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PmsCustomerProjectsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=50, unique=True, verbose_name='项目名称')),
                ('project_base', models.CharField(default='北东区', max_length=50, verbose_name='北东区域&南区')),
                ('project_num', models.CharField(default='未知', max_length=50, null=True, unique=True, verbose_name='项目编号')),
                ('project_owner', models.CharField(default='无', max_length=50, null=True, verbose_name='所属PM')),
                ('project_resident', models.CharField(default='无', max_length=50, null=True, verbose_name='驻场TM')),
                ('project_product', models.CharField(default='未知', max_length=50, null=True, verbose_name='部署产品')),
                ('project_update_time', models.CharField(default='无', max_length=50, null=True, verbose_name='更新日期')),
                ('project_update_user', models.CharField(default='无', max_length=50, null=True, verbose_name='操作人')),
                ('project_update_file', models.CharField(default='文件列表', max_length=50, null=True, verbose_name='更新文档')),
                ('project_ivc', models.CharField(default='追一自研', max_length=50, null=True, verbose_name='IVC')),
                ('project_db', models.CharField(default='追一自研', max_length=50, null=True, verbose_name='数据库')),
                ('project_middleware', models.CharField(default='追一自研', max_length=50, null=True, verbose_name='中间件')),
            ],
            options={
                'verbose_name': '定制化项目信息',
                'verbose_name_plural': '定制化项目信息',
                'db_table': 'pms_customer_projects_list',
            },
        ),
    ]
