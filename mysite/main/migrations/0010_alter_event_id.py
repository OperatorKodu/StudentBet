# Generated by Django 3.2.3 on 2021-06-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0009_remove_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
