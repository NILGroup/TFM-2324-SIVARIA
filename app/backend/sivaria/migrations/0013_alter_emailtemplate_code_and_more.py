# Generated by Django 4.2.13 on 2024-07-14 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sivaria", "0012_alter_emailtemplate_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="code",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="pushnotificationtype",
            name="slug",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="pushnotificationtype",
            name="title",
            field=models.TextField(max_length=80),
        ),
    ]
