# Generated by Django 4.0.6 on 2025-01-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_product_flesh_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Cheese',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='spicy',
            field=models.BooleanField(default=False),
        ),
    ]
