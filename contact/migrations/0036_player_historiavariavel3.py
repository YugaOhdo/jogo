# Generated by Django 4.2.8 on 2024-03-04 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0035_player_historiavariavel2'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='historiaVariavel3',
            field=models.IntegerField(default=1),
        ),
    ]