# Generated by Django 4.1.7 on 2023-04-27 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addquipments',
            old_name='manufacturedYear',
            new_name='ManufacturedYear',
        ),
    ]