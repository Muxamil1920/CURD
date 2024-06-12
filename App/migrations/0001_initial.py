# Generated by Django 5.0.6 on 2024-06-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField(max_length=280)),
                (
                    "file",
                    models.ImageField(null=True, unique=True, upload_to="products/"),
                ),
            ],
        ),
    ]