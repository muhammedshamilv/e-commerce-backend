# Generated by Django 4.2.7 on 2024-01-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_availability"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="uploads/"),
        ),
    ]