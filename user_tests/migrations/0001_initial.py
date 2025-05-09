# Generated by Django 5.1.4 on 2025-04-24 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("exam_sections", "0001_initial"),
        ("questions", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserTest",
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
                ("language_code", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_tests",
                        to="exam_sections.section",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_tests",
                        to="users.user",
                    ),
                ),
            ],
            options={
                "db_table": "user_tests",
            },
        ),
        migrations.CreateModel(
            name="TestQuestion",
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
                ("question_order", models.IntegerField(blank=True, null=True)),
                (
                    "variant_question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="questions.question",
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="test_questions",
                        to="user_tests.usertest",
                    ),
                ),
            ],
            options={
                "db_table": "test_questions",
            },
        ),
    ]
