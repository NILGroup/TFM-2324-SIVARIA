# Generated by Django 4.2.13 on 2024-07-01 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sivaria", "0005_alter_pushnotificationtype_data"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appuser",
            options={},
        ),
        migrations.AlterUniqueTogether(
            name="appuser",
            unique_together={("email",)},
        ),
    ]
