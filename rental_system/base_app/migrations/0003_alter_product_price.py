# Generated by Django 5.0 on 2023-12-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
