# Generated by Django 4.1.7 on 2023-04-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_addcrop_alter_user_contact_farmerkyc'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('age', models.CharField(max_length=225)),
            ],
        ),
    ]