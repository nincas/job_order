# Generated by Django 2.0.1 on 2018-03-24 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_order_sys', '0004_auto_20180324_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 24, 15, 40, 23, 793500)),
        ),
    ]
