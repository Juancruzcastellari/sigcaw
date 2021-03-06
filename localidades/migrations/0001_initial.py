# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('abreviatura', models.CharField(blank=True, max_length=255, null=True, verbose_name='Abreviatura')),
                ('codigo_postal', models.CharField(max_length=255, verbose_name='Codigo Postal')),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
                'ordering': ['provincia', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('abreviatura', models.CharField(blank=True, max_length=255, null=True, verbose_name='Abreviatura')),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('abreviatura', models.CharField(blank=True, max_length=255, null=True, verbose_name='Abreviatura')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pais', to='localidades.Pais', verbose_name='Pais')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'ordering': ['pais', 'nombre'],
            },
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincia', to='localidades.Provincia', verbose_name='Provincia'),
        ),
    ]
