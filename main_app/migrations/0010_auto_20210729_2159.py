# Generated by Django 3.2.5 on 2021-07-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210729_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro',
            name='experience',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='pro',
            name='goals',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]