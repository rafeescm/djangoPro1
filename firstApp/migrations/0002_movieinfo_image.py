# Generated by Django 5.0.1 on 2024-01-17 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]