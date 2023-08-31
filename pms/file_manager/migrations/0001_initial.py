# Generated by Django 4.2.2 on 2023-08-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PmsFilesManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(default='', max_length=50, unique=True, verbose_name='文件名称')),
                ('file_uuid', models.CharField(default='', max_length=50, unique=True, verbose_name='文件uuid')),
                ('file_type', models.CharField(default='未知', max_length=50, null=True, verbose_name='文件类型')),
                ('file_size', models.CharField(default='未知', max_length=50, null=True, verbose_name='文件大小')),
                ('file_project', models.CharField(default='未知', max_length=50, verbose_name='所属项目')),
                ('file_modify_time', models.CharField(default='无', max_length=50, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文件列表信息',
                'verbose_name_plural': '文件列表信息',
                'db_table': 'pms_files_manager',
            },
        ),
    ]
