# Generated by Django 4.2.8 on 2024-03-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0037_player_fase_atual'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='energy_pointFase1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='life_round2savepoint',
            field=models.IntegerField(default=0),
        ),
    ]
