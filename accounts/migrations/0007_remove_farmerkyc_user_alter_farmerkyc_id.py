# Generated by Django 4.1.7 on 2023-04-09 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_password_farmerkyc_passport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmerkyc',
            name='user',
        ),
        migrations.AlterField(
            model_name='farmerkyc',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]