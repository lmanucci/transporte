# Generated by Django 4.0.5 on 2022-08-09 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_Misviajes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viajes',
            name='Destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciudaddestino', to='app_Misviajes.localidades', verbose_name='Ciudad'),
        ),
    ]
