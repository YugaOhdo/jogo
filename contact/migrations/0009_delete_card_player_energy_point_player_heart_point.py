# Generated by Django 4.2.8 on 2024-01-19 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_remove_player_first_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.AddField(
            model_name='player',
            name='energy_point',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='player',
            name='heart_point',
            field=models.IntegerField(default=3),
        ),
    ]
