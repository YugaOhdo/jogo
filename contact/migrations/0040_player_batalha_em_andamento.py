# Generated by Django 4.2.8 on 2024-03-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0039_player_controle1'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='batalha_em_andamento',
            field=models.BooleanField(default=False),
        ),
    ]
