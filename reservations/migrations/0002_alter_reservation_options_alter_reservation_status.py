# Generated by Django 5.1.1 on 2024-09-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Reservation', 'verbose_name_plural': 'Reservations'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Canceled', 'Canceled')], default='Pending', max_length=12, verbose_name='Status'),
        ),
    ]
