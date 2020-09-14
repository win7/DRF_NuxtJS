# Generated by Django 3.1.1 on 2020-09-12 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Teléfono')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Propietario',
                'verbose_name_plural': 'Propietarios',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('birth_date', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('weight', models.FloatField(default=1, verbose_name='Peso')),
                ('kind_type', models.CharField(choices=[('k1', 'Perro'), ('k2', 'Gato'), ('k3', 'Canario'), ('k4', 'Hámster')], max_length=2, verbose_name='Especie')),
                ('description', models.TextField(max_length=200, verbose_name='Descripción')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyAPI.owner', verbose_name='Propietario')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'ordering': ['name'],
            },
        ),
    ]
