# Generated by Django 4.2.8 on 2024-01-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0016_player_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='atk_atual',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='atk_do_vilao',
            field=models.IntegerField(default=0),
        ),
    ]