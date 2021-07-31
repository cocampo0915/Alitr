# Generated by Django 3.2.4 on 2021-07-22 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=250)),
                ('date', models.DateField(verbose_name='date applied')),
                ('requirements', models.TextField(max_length=500)),
                ('notes', models.TextField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('status', models.CharField(choices=[('1', 'Applied'), ('2', 'In Progress'), ('3', 'Interview scheduled'), ('3', 'Interview complete'), ('3', 'Job Offer'), ('4', 'Incomplete'), ('5', 'Not Selected'), ('6', 'Unknown')], default='1', max_length=1)),
                ('job_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.job_application')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]