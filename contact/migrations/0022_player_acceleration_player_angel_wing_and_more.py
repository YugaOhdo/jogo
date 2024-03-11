# Generated by Django 4.2.8 on 2024-01-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0021_alter_player_enemy_life_round2'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='acceleration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='angel_wing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='calculo_dano_inimigo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='calculo_dano_player',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='dark_aura',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='dark_energy_blast',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='dark_energy_shield',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='millennium_shield',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='rising_enerny',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='thounsand_knives',
            field=models.BooleanField(default=False),
        ),
    ]
