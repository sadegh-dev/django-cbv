# Generated by Django 3.2.3 on 2021-05-23 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Book',
            new_name='book',
        ),
    ]
