# Generated by Django 4.1.1 on 2022-09-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                help_text="It's required and must be unique",
                max_length=255,
                verbose_name="Category Name",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=255, verbose_name="Category safe URL"),
        ),
    ]
