# Generated by Django 3.2.9 on 2021-11-04 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_scopes_article_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tag',
            new_name='scopes',
        ),
    ]
