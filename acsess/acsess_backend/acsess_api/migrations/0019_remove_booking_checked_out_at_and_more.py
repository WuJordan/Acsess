# Generated by Django 5.0.4 on 2024-07-30 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acsess_api', '0018_booking_checked_in_at_booking_checked_out_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='checked_out_at',
        ),
        migrations.RemoveField(
            model_name='booking_history',
            name='checked_out_at',
        ),
    ]
