# Generated by Django 4.2.7 on 2024-01-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="availability",
            field=models.IntegerField(default=0),
        ),
    ]
