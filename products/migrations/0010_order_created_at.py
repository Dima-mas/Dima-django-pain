# Generated by Django 4.2.7 on 2023-12-01 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_order_alter_product_category_orderproduct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 1, 15, 45, 47, 240576)),
        ),
    ]
