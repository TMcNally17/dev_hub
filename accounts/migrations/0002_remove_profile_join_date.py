# Generated by Django 2.0 on 2018-11-16 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='join_date',
        ),
    ]
