# Generated by Django 4.0.3 on 2022-09-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienci', '0014_wizyty_create_date_wizyty_visit_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wizyty',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='wizyty',
            name='visit_time',
        ),
        migrations.AlterField(
            model_name='wizyty',
            name='visit_date',
            field=models.DateTimeField(verbose_name='Data wizyty'),
        ),
    ]