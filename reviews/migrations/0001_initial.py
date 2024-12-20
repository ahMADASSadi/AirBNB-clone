# Generated by Django 5.1.1 on 2024-09-20 20:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0009_alter_roomimage_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('review_text', models.TextField(verbose_name='Review Text')),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Accuracy')),
                ('communication', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Communication')),
                ('cleanliness', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Cleanliness')),
                ('location', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Location')),
                ('check_in', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Check In')),
                ('value', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Value')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room', verbose_name='Room')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
