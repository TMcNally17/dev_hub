# Generated by Django 2.0 on 2018-12-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_url',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]