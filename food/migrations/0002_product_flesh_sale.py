# Generated by Django 4.0.6 on 2025-01-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='flesh_sale',
            field=models.BooleanField(default=False),
        ),
    ]
