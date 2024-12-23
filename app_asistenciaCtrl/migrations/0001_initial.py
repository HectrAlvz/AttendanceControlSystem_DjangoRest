# Generated by Django 5.1.4 on 2024-12-13 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la Empresa')),
                ('location', models.CharField(max_length=100, verbose_name='Ubicación')),
                ('established_date', models.DateField(verbose_name='Fecha de Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Trabajador')),
                ('position', models.CharField(max_length=100, verbose_name='Cargo')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='app_asistenciaCtrl.company', verbose_name='Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('present', models.BooleanField(default=False, verbose_name='Presente')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='app_asistenciaCtrl.worker', verbose_name='Trabajador')),
            ],
        ),
    ]
