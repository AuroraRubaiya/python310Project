# Generated by Django 3.1.7 on 2021-03-31 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20210331_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='set_avaibles',
            new_name='seat_available',
        ),
    ]