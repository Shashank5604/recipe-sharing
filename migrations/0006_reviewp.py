# Generated by Django 5.0.1 on 2024-03-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_rename_cards_card_rename_service1s_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=90)),
                ('remail', models.EmailField(max_length=90)),
                ('rmessage', models.TextField()),
            ],
        ),
    ]
