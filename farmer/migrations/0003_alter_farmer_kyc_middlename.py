# Generated by Django 4.1.7 on 2023-05-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_alter_farmer_kyc_citizenship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_kyc',
            name='MiddleName',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
