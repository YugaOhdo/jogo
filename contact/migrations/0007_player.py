# Generated by Django 4.2.8 on 2024-01-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_card_remove_contact_category_remove_contact_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
            ],
        ),
    ]
