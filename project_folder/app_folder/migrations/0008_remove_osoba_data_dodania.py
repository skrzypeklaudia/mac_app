# Generated by Django 5.1.4 on 2025-01-17 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_folder', '0007_alter_osoba_data_dodania'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='osoba',
            name='data_dodania',
        ),
    ]
