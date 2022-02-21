# Generated by Django 4.0.2 on 2022-02-21 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_travelfrom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Travel Date')),
                ('notes', models.TextField()),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.stop')),
            ],
        ),
    ]
