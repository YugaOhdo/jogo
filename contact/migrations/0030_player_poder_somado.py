# Generated by Django 4.2.8 on 2024-02-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0029_player_boss_escolhido_atk'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='poder_somado',
            field=models.IntegerField(default=0),
        ),
    ]
