# Generated by Django 2.2.6 on 2020-06-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200620_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcontent',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content', to='blog.Post'),
        ),
    ]
