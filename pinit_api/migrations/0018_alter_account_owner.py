# Generated by Django 4.2.5 on 2024-02-27 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinit_api', '0017_alter_pin_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
