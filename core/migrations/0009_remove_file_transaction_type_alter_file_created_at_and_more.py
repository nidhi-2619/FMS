# Generated by Django 5.0 on 2023-12-08 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_file_timestamp_file_transaction_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='transaction_type',
        ),
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 19, 34, 30, 830605)),
        ),
        migrations.DeleteModel(
            name='FileTransaction',
        ),
    ]