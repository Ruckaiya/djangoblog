# Generated by Django 2.2.2 on 2019-06-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0003_auto_20190622_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestpost',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
