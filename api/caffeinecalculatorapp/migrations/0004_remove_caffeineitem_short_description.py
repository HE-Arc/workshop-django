# Generated by Django 5.0 on 2024-01-09 10:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("caffeinecalculatorapp", "0003_caffeineitem_short_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="caffeineitem",
            name="short_description",
        ),
    ]