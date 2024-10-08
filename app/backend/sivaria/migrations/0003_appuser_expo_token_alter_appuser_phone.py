# Generated by Django 4.2.13 on 2024-06-27 15:27

from django.db import migrations, models
import sivaria.validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ("sivaria", "0002_remove_userhasparent_phone_parent_1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="appuser",
            name="expo_token",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="appuser",
            name="phone",
            field=models.CharField(
                help_text="The phone number must contain only digits and must be a Spanish number.",
                max_length=9,
                null=True,
                validators=[sivaria.validators.validators.SpanishPhoneValidator()],
            ),
        ),
    ]
