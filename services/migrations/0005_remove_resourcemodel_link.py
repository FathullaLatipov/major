# Generated by Django 5.1 on 2024-08-31 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_resourceimagesmodel_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcemodel',
            name='link',
        ),
    ]
