# Generated by Django 4.0.5 on 2022-07-08 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Misviajes', '0005_alter_viajes_camion'),
    ]

    operations = [
        migrations.CreateModel(
            name='camioneros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Completo', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
            ],
        ),
    ]
