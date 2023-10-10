# Generated by Django 4.2.5 on 2023-09-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Nosotras",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=200)),
                ("cargo", models.CharField(max_length=200)),
                ("grado", models.CharField(max_length=200)),
                ("voluntaria", models.BooleanField()),
            ],
        ),
    ]