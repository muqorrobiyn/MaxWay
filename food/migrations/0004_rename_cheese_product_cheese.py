# Generated by Django 4.0.6 on 2025-01-05 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_product_cheese_product_spicy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Cheese',
            new_name='cheese',
        ),
    ]