# Generated by Django 5.1.4 on 2025-01-21 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_folder', '0011_osoba_wlasciciel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko'], 'permissions': [('view_person_other_owner', 'Pozwala zobaczyć modele Osoba innych wlaścicieli')]},
        ),
    ]
