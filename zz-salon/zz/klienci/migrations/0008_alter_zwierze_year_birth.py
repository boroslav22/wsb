# Generated by Django 4.0.3 on 2022-09-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienci', '0007_alter_zwierze_city_alter_zwierze_last_visit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zwierze',
            name='year_birth',
            field=models.IntegerField(blank=True, default='2020', max_length=4, null=True, verbose_name='Data urodzenia'),
        ),
    ]
