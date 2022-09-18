# Generated by Django 4.0.3 on 2022-09-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klienci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gatunek', models.CharField(max_length=20, verbose_name='Gatunek')),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=10, verbose_name='Płeć')),
            ],
        ),
        migrations.CreateModel(
            name='Zwierze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
            ],
        ),
    ]
