# Generated by Django 3.1.6 on 2021-05-02 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogblog', '0006_auto_20210502_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='CodeId',
            new_name='codeId',
        ),
    ]
