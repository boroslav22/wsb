# Generated by Django 4.0.3 on 2022-09-07 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klienci', '0012_alter_zwierze_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wizyty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(verbose_name='Data wizyty')),
                ('zwierze', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='klienci.zwierze')),
            ],
            options={
                'verbose_name': 'Wizyty',
                'verbose_name_plural': 'Wizyty',
            },
        ),
    ]
