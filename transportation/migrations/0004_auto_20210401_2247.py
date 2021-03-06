# Generated by Django 3.1.7 on 2021-04-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0003_auto_20210401_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air',
            name='seat_available',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='air',
            name='time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_available',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bus',
            name='time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='train',
            name='seat_available',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='train',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
