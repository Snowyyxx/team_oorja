# Generated by Django 5.0.4 on 2024-05-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('sponsor_name', models.TextField()),
                ('sponsor_image', models.TextField()),
                ('sponsor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sponsor_description', models.TextField()),
            ],
        ),
    ]
