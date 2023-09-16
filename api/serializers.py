from rest_framework import serializers

from researches.models import Reference, Score, Test


class ScoresSerializer(serializers.ModelSerializer):
    indicator_name = serializers.CharField(
        source='indicator_metric.indicator.name',
    )
    metric_name = serializers.CharField(
        source='indicator_metric.metric.name',
    )
    metric_unit = serializers.CharField(
        source='indicator_metric.metric.unit',
    )
    is_within_normal_range = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = (
            'id',
            'score',
            'indicator_name',
            'metric_name',
            'metric_unit',
            'is_within_normal_range',
        )

    def get_is_within_normal_range(self, obj: Score) -> bool:
        reference = Reference.objects.get(
            indicator_metric=obj.indicator_metric,
        )
        return reference.min_score <= obj.score <= reference.max_score


class TestsSerializer(serializers.ModelSerializer):
    lab_id = serializers.IntegerField(source='lab.id')
    duration_seconds = serializers.SerializerMethodField()
    results = ScoresSerializer(
        many=True,
        source='test_score',
    )

    class Meta:
        model = Test
        fields = (
            'id',
            'lab_id',
            'duration_seconds',
            'results',
        )

    def get_duration_seconds(self, obj: Test) -> int:
        return int((obj.completed_at - obj.started_at).total_seconds())
