# Generated by Django 4.2.5 on 2024-02-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pinit_api", "0022_remove_account_saved_pins_account_pin_saves"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="pin_saves",
        ),
        migrations.AddField(
            model_name="account",
            name="saved_pins",
            field=models.ManyToManyField(
                related_name="saved_by", through="pinit_api.PinSave", to="pinit_api.pin"
            ),
        ),
    ]
