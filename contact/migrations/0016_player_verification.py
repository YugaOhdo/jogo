# Generated by Django 4.2.8 on 2024-01-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0015_player_atk_do_vilao_player_carta_do_vilao'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='verification',
            field=models.FloatField(default=False),
        ),
    ]