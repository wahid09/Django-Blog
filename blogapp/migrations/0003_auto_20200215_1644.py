# Generated by Django 2.2.6 on 2020-02-15 10:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20200211_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
