# Generated by Django 4.0.3 on 2022-09-04 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klienci', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zwierze',
            options={'verbose_name': 'Zwierze', 'verbose_name_plural': 'Zwierzaki'},
        ),
        migrations.AddField(
            model_name='zwierze',
            name='breed',
            field=models.CharField(max_length=30, null=True, verbose_name='Rasa'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='city',
            field=models.CharField(default='Brzoza', max_length=20, verbose_name='Miejscowość'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='comments',
            field=models.TextField(blank=True, verbose_name='Uwagi'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='create_date',
            field=models.DateField(auto_now=True, verbose_name='Data dodania'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='adres email'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='gatunek',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='klienci.animaltype'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='last_visit',
            field=models.DateField(default='2000-01-01', verbose_name='Ostatnia wizyta'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='next_visit',
            field=models.DateField(null=True, verbose_name='Następna wizyta'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='owner',
            field=models.CharField(max_length=20, null=True, verbose_name='Właściciel'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, verbose_name='Kontakt'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='sex',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='klienci.sex'),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='zwierze',
            name='year_birth',
            field=models.IntegerField(default='2000', verbose_name='Data urodzenia'),
        ),
    ]