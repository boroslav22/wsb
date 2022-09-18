# Generated by Django 4.0.3 on 2022-09-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienci', '0006_alter_zwierze_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zwierze',
            name='city',
            field=models.CharField(blank=True, default='Brzoza', max_length=20, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='zwierze',
            name='last_visit',
            field=models.DateField(blank=True, null=True, verbose_name='Ostatnia wizyta'),
        ),
        migrations.AlterField(
            model_name='zwierze',
            name='next_visit',
            field=models.DateField(blank=True, null=True, verbose_name='Następna wizyta'),
        ),
        migrations.AlterField(
            model_name='zwierze',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='zwierze',
            name='year_birth',
            field=models.IntegerField(blank=True, max_length=4, null=True, verbose_name='Data urodzenia'),
        ),
    ]