# Generated by Django 4.1.7 on 2023-04-29 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0004_delete_addquipments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipments',
            name='Photo',
            field=models.ImageField(upload_to='images/crops'),
        ),
    ]