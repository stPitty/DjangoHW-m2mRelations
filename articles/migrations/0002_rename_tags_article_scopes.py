# Generated by Django 3.2.9 on 2021-11-04 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='scopes',
        ),
    ]
