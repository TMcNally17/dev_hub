# Generated by Django 2.0 on 2018-12-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blog_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
