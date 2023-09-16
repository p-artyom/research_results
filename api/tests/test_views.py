from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework.test import APIClient

User = get_user_model()


class ViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = mixer.blend(User)

        cls.indicators = mixer.blend('researches.Indicator')
        cls.metrics = mixer.blend('researches.Metric')
        cls.indicators_metrics = mixer.blend(
            'researches.IndicatorMetric',
            indicator=cls.indicators,
            metric=cls.metrics,
        )
        cls.tests = mixer.blend('researches.Test')
        cls.scores = mixer.blend(
            'researches.Score',
            test=cls.tests,
            indicator_metric=cls.indicators_metrics,
        )
        cls.references = mixer.blend(
            'researches.Reference',
            indicator_metric=cls.indicators_metrics,
        )

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.authorized_user = APIClient()
        cls.authorized_user.force_authenticate(cls.user)

        cls.urls = {
            'test': f'/api/v1/tests/{cls.tests.id}/',
        }

    def test_views(self) -> None:
        """Результат исследования содержит ожидаемые поля."""

        urls_users_data = (
            (
                self.urls.get('test'),
                self.client,
                {
                    'detail': 'Учетные данные не были предоставлены.',
                },
            ),
            (
                self.urls.get('test'),
                self.authorized_user,
                {
                    'id': self.tests.id,
                    'lab_id': self.tests.lab.id,
                    'duration_seconds': int(
                        (
                            self.tests.completed_at - self.tests.started_at
                        ).total_seconds(),
                    ),
                    'results': [
                        {
                            'id': self.scores.id,
                            'score': str(self.scores.score),
                            'indicator_name': self.indicators.name,
                            'metric_name': self.metrics.name,
                            'metric_unit': self.metrics.unit,
                            'is_within_normal_range': self.references.min_score
                            <= self.scores.score
                            <= self.references.max_score,
                        },
                    ],
                },
            ),
        )
        for url, user, data in urls_users_data:
            with self.subTest(url=url, user=user, data=data):
                self.assertEqual(
                    user.get(url).json(),
                    data,
                )
