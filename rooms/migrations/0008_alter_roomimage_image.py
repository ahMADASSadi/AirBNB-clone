# Generated by Django 5.1.1 on 2024-09-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_roomimage_delete_roomphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomimage',
            name='image',
            field=models.ImageField(upload_to='rooms/images', verbose_name='Image'),
        ),
    ]
