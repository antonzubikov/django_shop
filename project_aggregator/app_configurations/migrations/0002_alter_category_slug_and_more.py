# Generated by Django 4.1.7 on 2023-05-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_configurations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                max_length=100, unique=True, verbose_name="URL категории"
            ),
        ),
        migrations.AlterField(
            model_name="sitesettings",
            name="cost_express_delivery",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Цена экспресс доставки",
                max_digits=10,
                verbose_name="Экспресс",
            ),
        ),
        migrations.AlterField(
            model_name="sitesettings",
            name="cost_usual_delivery",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Цена обычной доставки",
                max_digits=10,
                verbose_name="Обычная",
            ),
        ),
    ]
