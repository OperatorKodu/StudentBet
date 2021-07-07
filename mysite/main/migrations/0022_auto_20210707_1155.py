# Generated by Django 3.2.4 on 2021-07-07 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_coupon_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='datetime',
            new_name='start_datetime',
        ),
        migrations.AddField(
            model_name='category',
            name='duration',
            field=models.IntegerField(default=60, help_text='Enter duration of the event'),
        ),
        migrations.AddField(
            model_name='event',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='event',
            name='is_settled',
            field=models.BooleanField(default=False),
        ),
    ]
