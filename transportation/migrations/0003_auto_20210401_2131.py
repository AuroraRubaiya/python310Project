# Generated by Django 3.1.7 on 2021-04-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0002_auto_20210401_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='train',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
