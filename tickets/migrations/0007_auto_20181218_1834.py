# Generated by Django 2.0 on 2018-12-18 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_remove_ticket_forum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
