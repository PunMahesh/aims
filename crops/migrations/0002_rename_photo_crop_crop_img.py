# Generated by Django 4.1.7 on 2023-04-30 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='photo',
            new_name='crop_img',
        ),
    ]
