# Generated by Django 5.0 on 2024-01-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("caffeinecalculatorapp", "0002_consumeditem"),
    ]

    operations = [
        migrations.AddField(
            model_name="caffeineitem",
            name="short_description",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]