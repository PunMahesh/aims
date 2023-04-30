# Generated by Django 4.1.7 on 2023-04-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=225)),
                ('pesticide_used', models.CharField(max_length=225)),
                ('market_value', models.CharField(max_length=10)),
                ('disease', models.CharField(blank=True, max_length=225, null=True)),
                ('season', models.CharField(max_length=225)),
                ('photo', models.ImageField(upload_to='images/crops')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]