# Generated by Django 2.2.6 on 2020-06-19 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200619_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='headline',
        ),
        migrations.AddField(
            model_name='postcontent',
            name='content',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcontent',
            name='headline',
            field=models.CharField(default='q', max_length=20),
            preserve_default=False,
        ),
    ]
