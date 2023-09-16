from django.contrib import admin

from core.admin import BaseAdmin
from researches.models import (
    Indicator,
    IndicatorMetric,
    Lab,
    Metric,
    Reference,
    Score,
    Test,
)


@admin.register(Lab)
class LabAdmin(BaseAdmin):
    list_display = ('pk', 'name', 'is_active', 'created', 'modified')
    search_fields = ('name',)


@admin.register(Test)
class TestAdmin(BaseAdmin):
    list_display = (
        'pk',
        'started_at',
        'completed_at',
        'comment',
        'lab',
        'is_active',
        'created',
        'modified',
    )
    list_editable = ('lab',)
    search_fields = ('pk',)


@admin.register(Indicator)
class IndicatorAdmin(BaseAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'is_active',
        'created',
        'modified',
    )
    search_fields = ('name',)


@admin.register(Metric)
class MetricAdmin(BaseAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'unit',
        'is_active',
        'created',
        'modified',
    )
    search_fields = ('name',)


@admin.register(IndicatorMetric)
class IndicatorMetricAdmin(BaseAdmin):
    list_display = (
        'pk',
        'indicator',
        'metric',
        'is_active',
        'created',
        'modified',
    )
    list_editable = (
        'indicator',
        'metric',
    )
    search_fields = ('pk',)


@admin.register(Score)
class ScoreAdmin(BaseAdmin):
    list_display = (
        'pk',
        'score',
        'test',
        'indicator_metric',
        'is_active',
        'created',
        'modified',
    )
    list_editable = (
        'test',
        'indicator_metric',
    )
    search_fields = ('pk',)


@admin.register(Reference)
class ReferenceAdmin(BaseAdmin):
    list_display = (
        'pk',
        'min_score',
        'max_score',
        'indicator_metric',
        'created',
        'modified',
    )
    list_editable = ('indicator_metric',)
    search_fields = ('pk',)
