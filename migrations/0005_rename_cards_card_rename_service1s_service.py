# Generated by Django 5.0.1 on 2024-02-28 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_cards_ima'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cards',
            new_name='card',
        ),
        migrations.RenameModel(
            old_name='service1s',
            new_name='service',
        ),
    ]
