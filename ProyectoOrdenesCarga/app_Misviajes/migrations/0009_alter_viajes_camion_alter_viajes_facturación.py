# Generated by Django 4.0.5 on 2022-07-09 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Misviajes', '0008_alter_viajes_origen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viajes',
            name='Camion',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='viajes',
            name='Facturación',
            field=models.CharField(max_length=30),
        ),
    ]
