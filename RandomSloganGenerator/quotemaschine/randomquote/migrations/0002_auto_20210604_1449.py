# Generated by Django 3.2.3 on 2021-06-04 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('randomquote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='color',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='parti',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
