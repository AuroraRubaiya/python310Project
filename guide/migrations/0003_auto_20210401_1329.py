# Generated by Django 3.1.7 on 2021-04-01 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_auto_20210401_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='avaibles',
            new_name='available',
        ),
    ]