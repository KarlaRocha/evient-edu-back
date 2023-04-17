# Generated by Django 4.1.2 on 2023-04-17 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("player", "0002_alter_player_draws_alter_player_loses_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
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
                ("created_date", models.DateField()),
                ("updated_date", models.DateField()),
                ("symbol", models.TextField()),
                ("active", models.BooleanField(default=True)),
                ("is_draw", models.BooleanField(default=False)),
                (
                    "player_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player1_matches",
                        to="player.player",
                    ),
                ),
                (
                    "player_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player2_matches",
                        to="player.player",
                    ),
                ),
                (
                    "turn",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="current_turn",
                        to="player.player",
                    ),
                ),
                (
                    "winner",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="winner",
                        to="player.player",
                    ),
                ),
            ],
        ),
    ]
