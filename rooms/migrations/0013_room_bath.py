# Generated by Django 5.1.1 on 2024-09-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0012_rename_desciption_room_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='bath',
            field=models.SmallIntegerField(default=1, verbose_name='Bath'),
            preserve_default=False,
        ),
    ]
