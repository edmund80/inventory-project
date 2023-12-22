# Generated by Django 5.0 on 2023-12-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("itemName", models.CharField(max_length=50)),
                ("itemLocation", models.CharField(max_length=50)),
                ("itemQuantity", models.IntegerField()),
                ("dateAdded", models.DateField()),
            ],
        ),
    ]
