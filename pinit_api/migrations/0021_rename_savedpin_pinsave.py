# Generated by Django 4.2.5 on 2024-02-29 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinit_api', '0020_rename_saved_at_savedpin_last_saved_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SavedPin',
            new_name='PinSave',
        ),
    ]
