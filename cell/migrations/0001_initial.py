# Generated by Django 4.1.2 on 2023-04-26 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("match", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cell",
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
                ("row", models.SmallIntegerField()),
                ("column", models.SmallIntegerField()),
                ("symbol", models.TextField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="match.match"
                    ),
                ),
            ],
        ),
    ]
