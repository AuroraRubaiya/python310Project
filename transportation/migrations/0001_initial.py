# Generated by Django 3.1.7 on 2021-03-31 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='train',
            fields=[
                ('train_code', models.IntegerField(primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField()),
                ('seat_available', models.CharField(max_length=15)),
                ('time', models.IntegerField()),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='place.current_place')),
            ],
        ),
        migrations.CreateModel(
            name='bus',
            fields=[
                ('bus_code', models.IntegerField(primary_key=True, serialize=False)),
                ('bus_name', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField()),
                ('seat_available', models.CharField(max_length=15)),
                ('time', models.IntegerField()),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='place.current_place')),
            ],
        ),
        migrations.CreateModel(
            name='air',
            fields=[
                ('air_code', models.IntegerField(primary_key=True, serialize=False)),
                ('air_name', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField()),
                ('seat_available', models.CharField(max_length=15)),
                ('time', models.IntegerField()),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='place.current_place')),
            ],
        ),
    ]
