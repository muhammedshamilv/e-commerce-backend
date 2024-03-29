# Generated by Django 4.2.7 on 2024-01-08 05:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="products",
            new_name="product",
        ),
        migrations.AlterUniqueTogether(
            name="cart",
            unique_together={("user", "product")},
        ),
    ]
