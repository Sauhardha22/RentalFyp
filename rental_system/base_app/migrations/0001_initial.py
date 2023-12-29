# Generated by Django 5.0 on 2023-12-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
