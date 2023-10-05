# Generated by Django 4.2.5 on 2023-10-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=63, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("deadline_date", models.DateTimeField(blank=True, null=True)),
                ("is_done", models.BooleanField(default=False)),
                ("tags", models.ManyToManyField(blank=True, to="tasks.tag")),
            ],
        ),
    ]
