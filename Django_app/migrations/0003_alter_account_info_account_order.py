# Generated by Django 4.1.1 on 2022-10-15 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_app', '0002_alter_account_info_account_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_info',
            name='account_order',
            field=models.DateField(default=datetime.datetime(2022, 10, 15, 21, 44, 56, 161288)),
        ),
    ]
