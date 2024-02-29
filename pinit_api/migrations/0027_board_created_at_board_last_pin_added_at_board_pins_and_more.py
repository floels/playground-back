# Generated by Django 5.0 on 2024-02-29 13:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pinit_api", "0026_rename_owner_board_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="board",
            name="last_pin_added_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="board",
            name="pins",
            field=models.ManyToManyField(
                related_name="boards",
                through="pinit_api.PinInBoard",
                to="pinit_api.pin",
            ),
        ),
        migrations.AlterField(
            model_name="pininboard",
            name="board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pins_in_board",
                to="pinit_api.board",
            ),
        ),
    ]
