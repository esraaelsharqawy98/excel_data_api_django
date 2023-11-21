# Generated by Django 4.2.7 on 2023-11-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('location_find', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]
