# Generated by Django 4.2.5 on 2023-10-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinit_api', '0013_alter_pin_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='unique_id',
            field=models.CharField(editable=False, max_length=18, unique=True),
        ),
    ]