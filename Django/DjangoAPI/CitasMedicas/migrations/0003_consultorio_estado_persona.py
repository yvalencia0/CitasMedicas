# Generated by Django 3.1.3 on 2020-11-03 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CitasMedicas', '0002_auto_20201103_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('cod_con', models.AutoField(primary_key=True, serialize=False)),
                ('des_con', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('cod_est', models.AutoField(primary_key=True, serialize=False)),
                ('des_est', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cod_per', models.AutoField(primary_key=True, serialize=False)),
                ('nom_per', models.CharField(max_length=100)),
                ('fna_per', models.CharField(max_length=100)),
                ('dir_per', models.CharField(max_length=100)),
                ('ema_per', models.CharField(max_length=100)),
                ('usu_per', models.CharField(max_length=100)),
                ('pas_per', models.CharField(max_length=100)),
            ],
        ),
    ]