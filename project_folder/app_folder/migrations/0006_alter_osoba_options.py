# Generated by Django 5.1.4 on 2025-01-15 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_folder', '0005_alter_osoba_plec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
    ]
