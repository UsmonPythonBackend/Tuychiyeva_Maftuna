# Generated by Django 5.1 on 2024-08-19 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servic', '0002_services_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
