# Generated by Django 5.0 on 2023-12-29 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ApplicationUser',
        ),
    ]