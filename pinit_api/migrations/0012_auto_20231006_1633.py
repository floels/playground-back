# Generated by Django 4.2.5 on 2023-10-06 16:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pinit_api", "0011_pin_unique_id_alter_pin_id"),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE INDEX pin_title_lower_idx ON pinit_api_pin (LOWER(title));
            CREATE INDEX pin_description_lower_idx ON pinit_api_pin (LOWER(description));
        """,
            """
            DROP INDEX IF EXISTS pin_title_lower_idx;
            DROP INDEX IF EXISTS pin_description_lower_idx;
        """,
        )
    ]
