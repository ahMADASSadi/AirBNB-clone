# Generated by Django 5.1.1 on 2024-10-25 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0016_alter_room_house_rule_alter_room_room_amenity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rooms.room', verbose_name='Room'),
        ),
    ]
