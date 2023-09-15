from django.db import models

from core.models import TimestampedModel
from core.utils import cut_string


class Lab(TimestampedModel):
    name = models.TextField(
        'название',
    )

    class Meta:
        verbose_name = 'лаборатория'
        verbose_name_plural = 'лаборатории'

    def __str__(self) -> str:
        return cut_string(self.name)


class Test(TimestampedModel):
    started_at = models.DateTimeField(
        verbose_name='дата начала',
    )
    completed_at = models.DateTimeField(
        verbose_name='дата окончания',
    )
    comment = models.TextField(
        'комментарий',
        blank=True,
    )
    lab = models.ForeignKey(
        Lab,
        on_delete=models.CASCADE,
        verbose_name='лаборатория',
    )

    class Meta:
        verbose_name = 'исследование'
        verbose_name_plural = 'исследования'

    def __str__(self) -> str:
        return cut_string(
            f'`{self.lab}` провела исследование под номером `{self.pk}`',
        )


class Indicator(TimestampedModel):
    name = models.TextField(
        'название',
    )
    description = models.TextField(
        'описание',
        blank=True,
    )

    class Meta:
        verbose_name = 'показатель'
        verbose_name_plural = 'показатели'

    def __str__(self) -> str:
        return cut_string(self.name)


class Metric(TimestampedModel):
    name = models.TextField(
        'название',
    )
    description = models.TextField(
        'описание',
        blank=True,
    )
    unit = models.TextField(
        'единица измерения',
    )

    class Meta:
        verbose_name = 'метрика'
        verbose_name_plural = 'метрики'

    def __str__(self) -> str:
        return cut_string(self.name)


class IndicatorMetric(TimestampedModel):
    indicator = models.ForeignKey(
        Indicator,
        on_delete=models.CASCADE,
        verbose_name='показатель',
    )
    metric = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        verbose_name='метрика',
    )

    class Meta:
        verbose_name = 'показатель-метрика'
        verbose_name_plural = 'показатели-метрики'

    def __str__(self) -> str:
        return cut_string(
            f'Показатель `{self.indicator.name}` состоит из '
            f'метрики `{self.metric.name}`',
        )


class Score(TimestampedModel):
    score = models.DecimalField(
        'значение',
        max_digits=10,
        decimal_places=5,
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='test_score',
        verbose_name='исследование',
    )
    indicator_metric = models.ForeignKey(
        IndicatorMetric,
        on_delete=models.CASCADE,
        verbose_name='показатель-метрика',
    )

    class Meta:
        verbose_name = 'фактическое значение'
        verbose_name_plural = 'фактические значения'
        constraints = [
            models.UniqueConstraint(
                fields=['test', 'indicator_metric'],
                name='unique_score',
            ),
        ]

    def __str__(self) -> str:
        return cut_string(
            f'Тест №{self.test.pk} измерил '
            f'`{self.indicator_metric.indicator.name}`',
        )


class Reference(TimestampedModel):
    min_score = models.DecimalField(
        'минимальное значение',
        max_digits=10,
        decimal_places=2,
    )
    max_score = models.DecimalField(
        'максимальное значение',
        max_digits=10,
        decimal_places=2,
    )
    indicator_metric = models.OneToOneField(
        IndicatorMetric,
        on_delete=models.CASCADE,
        verbose_name='показатель-метрика',
    )

    class Meta:
        verbose_name = 'нормальное значение'
        verbose_name_plural = 'нормальные значения'

    def __str__(self) -> str:
        return cut_string(
            f'Коридор нормальных значений {self.min_score}-{self.max_score} '
            f'для `{self.indicator_metric.indicator.name}`',
        )
