# Generated by Django 4.2.2 on 2023-09-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationHistory', '0002_alter_pmsoperationlogs_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pmsoperationlogs',
            name='project_name',
            field=models.CharField(default='', max_length=50, verbose_name='项目名称'),
        ),
    ]
