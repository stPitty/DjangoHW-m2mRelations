# Generated by Django 3.2.9 on 2021-11-04 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211105_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scopes',
            new_name='tag',
        ),
    ]