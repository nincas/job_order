# Generated by Django 2.0.1 on 2018-03-19 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_order_sys', '0004_auto_20180319_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_1',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_10',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_11',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_12',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_13',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_2',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_3',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_4',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_5',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_6',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_7',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_8',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megaa',
            name='jo_payment_date_9',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_1',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_10',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_11',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_12',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_13',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_2',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_3',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_4',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_5',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_6',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_7',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_8',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='megab',
            name='jo_payment_date_9',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 19, 19, 30, 38, 731708)),
        ),
    ]
