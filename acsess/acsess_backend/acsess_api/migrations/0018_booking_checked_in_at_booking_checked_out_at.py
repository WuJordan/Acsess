# Generated by Django 5.0.4 on 2024-07-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acsess_api', '0017_booking_check_in_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='checked_in_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='checked_out_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
