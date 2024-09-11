# Generated by Django 5.0.1 on 2024-03-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_alter_bookings_bdtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=50)),
                ('foodimage', models.FileField(default=None, max_length=250, null=True, upload_to='photo/')),
                ('foodprice', models.CharField(max_length=50)),
                ('foodmessage', models.TextField(max_length=90)),
            ],
        ),
        migrations.DeleteModel(
            name='card',
        ),
    ]
