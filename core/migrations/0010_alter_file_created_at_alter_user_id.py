# Generated by Django 5.0 on 2023-12-08 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_file_transaction_type_alter_file_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 19, 40, 25, 953671)),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
