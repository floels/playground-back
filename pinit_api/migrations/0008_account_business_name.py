# Generated by Django 4.1.7 on 2023-05-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pinit_api", "0007_remove_pin_text_remove_user_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="business_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
