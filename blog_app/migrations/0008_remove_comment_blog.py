# Generated by Django 4.2.1 on 2023-08-16 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
    ]
