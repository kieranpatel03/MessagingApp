# Generated by Django 4.1.4 on 2023-01-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TotalMessages",
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
                ("user_to", models.IntegerField()),
                ("user_sent", models.IntegerField()),
                ("last_message", models.CharField(max_length=1000)),
                ("last_date_sent", models.DateField()),
                ("unread_messages", models.IntegerField()),
            ],
        ),
    ]
