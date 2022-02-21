# Generated by Django 4.0.2 on 2022-02-21 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('arrival', models.DateField(verbose_name='Arrival Date')),
                ('departure', models.DateField(verbose_name='Departure Date')),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
            ],
        ),
        migrations.CreateModel(
            name='TravelTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Travel Date')),
                ('departure_time', models.CharField(max_length=50)),
                ('arrival_time', models.CharField(max_length=50)),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.stop')),
            ],
        ),
        migrations.AddField(
            model_name='stop',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.trips'),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Reservation Date')),
                ('time', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.stop')),
            ],
        ),
    ]
