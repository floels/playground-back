# Generated by Django 4.2.5 on 2024-02-29 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pinit_api", "0018_alter_account_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="SavedPin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("saved_at", models.DateTimeField(auto_now_add=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinit_api.account",
                    ),
                ),
                (
                    "pin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pinit_api.pin"
                    ),
                ),
            ],
            options={
                "unique_together": {("pin", "account")},
            },
        ),
        migrations.AddField(
            model_name="account",
            name="saved_pins",
            field=models.ManyToManyField(
                related_name="saved_by",
                through="pinit_api.SavedPin",
                to="pinit_api.pin",
            ),
        ),
    ]
