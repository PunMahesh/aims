# Generated by Django 4.1.7 on 2023-05-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='my_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]