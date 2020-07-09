# Generated by Django 2.2.6 on 2020-06-20 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_postcontent_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postcontent',
        ),
        migrations.AddField(
            model_name='postcontent',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Post'),
        ),
    ]
