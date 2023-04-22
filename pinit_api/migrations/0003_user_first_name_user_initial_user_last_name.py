# Generated by Django 4.1.7 on 2023-04-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pinit_api", "0002_alter_user_managers_user_is_admin"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="initial",
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]