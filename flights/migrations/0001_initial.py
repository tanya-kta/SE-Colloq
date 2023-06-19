# Generated by Django 4.2 on 2023-06-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('where_from', models.TextField()),
                ('where_to', models.TextField()),
                ('arrival_time', models.DateTimeField(blank=True)),
                ('departure_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
