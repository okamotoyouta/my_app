# Generated by Django 2.2.6 on 2020-06-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Unknown', max_length=12),
            preserve_default=False,
        ),
    ]
