# Generated by Django 3.2.15 on 2022-12-25 07:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField()),
                ('mail', models.EmailField(blank=True, max_length=50, null=True)),
                ('estado_respuesta', models.CharField(blank=True, choices=[('Contestada', 'Contestada'), ('No Contestada', 'No Contestada'), ('En proceso', 'En proceso')], default='No Contestada', max_length=15, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField()),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
                ('consulta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacto.consulta')),
            ],
        ),
    ]
