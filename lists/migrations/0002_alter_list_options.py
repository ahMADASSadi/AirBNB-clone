# Generated by Django 5.1.1 on 2024-09-21 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'verbose_name': 'List', 'verbose_name_plural': 'Lists'},
        ),
    ]
