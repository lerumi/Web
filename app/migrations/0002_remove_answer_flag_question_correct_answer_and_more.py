# Generated by Django 4.1 on 2023-11-15 00:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="flag",
        ),
        migrations.AddField(
            model_name="question",
            name="correct_answer",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="app.answer",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="created_date",
            field=models.DateTimeField(
                db_index=True, default=django.utils.timezone.now
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="rating",
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name="question",
            name="tags",
            field=models.ManyToManyField(
                blank=True, max_length=3, null=True, to="app.tag"
            ),
        ),
        migrations.CreateModel(
            name="QuestionLike",
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
                ("is_like", models.BooleanField(default=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.question"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("nick_name", models.CharField(blank=True, max_length=20)),
                (
                    "avatar",
                    models.ImageField(default="avatars/user.png", upload_to="avatars"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="app.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnswerLike",
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
                ("is_like", models.BooleanField(default=True)),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.answer"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.user"
                    ),
                ),
            ],
        ),
    ]