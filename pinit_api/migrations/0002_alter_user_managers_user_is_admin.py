# Generated by Django 4.1.7 on 2023-03-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pinit_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
