# Generated by Django 4.0.3 on 2022-09-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienci', '0009_alter_zwierze_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zwierze',
            name='year_birth',
            field=models.IntegerField(blank=True, default='2020', null=True, verbose_name='Data urodzenia'),
        ),
    ]
