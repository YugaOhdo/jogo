# Generated by Django 4.2.8 on 2024-01-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_player_heart_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='villain_strike_left',
            field=models.IntegerField(default=3),
        ),
    ]