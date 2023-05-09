# Generated by Django 4.1.7 on 2023-05-09 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_kyc',
            name='Citizenship',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\d+(-\\d+)*$')]),
        ),
        migrations.AlterField(
            model_name='farmer_kyc',
            name='Passport',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\d+(-\\d+)*$')]),
        ),
    ]