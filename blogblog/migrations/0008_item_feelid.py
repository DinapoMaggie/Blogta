# Generated by Django 3.1.6 on 2021-05-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogblog', '0007_auto_20210502_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='feelId',
            field=models.TextField(default=''),
        ),
    ]
