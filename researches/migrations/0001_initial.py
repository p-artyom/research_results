import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Indicator",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("is_active", models.BooleanField(verbose_name="активен")),
                ("name", models.TextField(verbose_name="название")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="описание"),
                ),
            ],
            options={
                "verbose_name": "показатель",
                "verbose_name_plural": "показатели",
            },
        ),
        migrations.CreateModel(
            name="IndicatorMetric",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("is_active", models.BooleanField(verbose_name="активен")),
                (
                    "indicator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="researches.indicator",
                        verbose_name="показатель",
                    ),
                ),
            ],
            options={
                "verbose_name": "показатель-метрика",
                "verbose_name_plural": "показатели-метрики",
            },
        ),
        migrations.CreateModel(
            name="Lab",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("is_active", models.BooleanField(verbose_name="активен")),
                ("name", models.TextField(verbose_name="название")),
            ],
            options={
                "verbose_name": "лаборатория",
                "verbose_name_plural": "лаборатории",
            },
        ),
        migrations.CreateModel(
            name="Metric",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("is_active", models.BooleanField(verbose_name="активен")),
                ("name", models.TextField(verbose_name="название")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="описание"),
                ),
                ("unit", models.TextField(verbose_name="единица измерения")),
            ],
            options={
                "verbose_name": "метрика",
                "verbose_name_plural": "метрики",
            },
        ),
        migrations.CreateModel(
            name="Test",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("is_active", models.BooleanField(verbose_name="активен")),
                (
                    "started_at",
                    models.DateTimeField(verbose_name="дата начала"),
                ),
                (
                    "completed_at",
                    models.DateTimeField(verbose_name="дата окончания"),
                ),
                (
                    "comment",
                    models.TextField(blank=True, verbose_name="комментарий"),
                ),
                (
                    "lab",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="researches.lab",
                        verbose_name="лаборатория",
                    ),
                ),
            ],
            options={
                "verbose_name": "исследование",
                "verbose_name_plural": "исследования",
            },
        ),
        migrations.CreateModel(
            name="Score",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("is_active", models.BooleanField(verbose_name="активен")),
                (
                    "score",
                    models.DecimalField(
                        decimal_places=5,
                        max_digits=10,
                        verbose_name="значение",
                    ),
                ),
                (
                    "indicator_metric",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="researches.indicatormetric",
                        verbose_name="показатель-метрика",
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="test_score",
                        to="researches.test",
                        verbose_name="исследование",
                    ),
                ),
            ],
            options={
                "verbose_name": "фактическое значение",
                "verbose_name_plural": "фактические значения",
            },
        ),
        migrations.CreateModel(
            name="Reference",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("is_active", models.BooleanField(verbose_name="активен")),
                (
                    "min_score",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="минимальное значение",
                    ),
                ),
                (
                    "max_score",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="максимальное значение",
                    ),
                ),
                (
                    "indicator_metric",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="researches.indicatormetric",
                        verbose_name="показатель-метрика",
                    ),
                ),
            ],
            options={
                "verbose_name": "нормальное значение",
                "verbose_name_plural": "нормальные значения",
            },
        ),
        migrations.AddField(
            model_name="indicatormetric",
            name="metric",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="researches.metric",
                verbose_name="метрика",
            ),
        ),
        migrations.AddConstraint(
            model_name="score",
            constraint=models.UniqueConstraint(
                fields=("test", "indicator_metric"), name="unique_score",
            ),
        ),
    ]
