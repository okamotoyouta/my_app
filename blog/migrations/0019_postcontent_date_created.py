# Generated by Django 2.2.6 on 2020-06-20 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200620_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcontent',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]