# Generated by Django 4.0.3 on 2022-09-12 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klienci', '0016_wizyty_create_date_wizyty_visit_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wizyty',
            name='zwierze',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klienci.zwierze'),
        ),
    ]
