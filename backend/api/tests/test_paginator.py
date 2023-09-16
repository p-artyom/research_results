from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework.test import APIClient

User = get_user_model()


class PaginatorTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = mixer.blend(User)

        cls.tests = mixer.cycle(
            settings.NUM_OBJECTS_ON_PAGE
            + settings.NUM_OBJECTS_ON_LAST_PAGE_FOR_TEST,
        ).blend('researches.Test')

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.authorized_user = APIClient()
        cls.authorized_user.force_authenticate(cls.user)

    def test_paginations(self) -> None:
        """Результаты исследований содержат ожидаемое количество объектов."""

        urls_num_objects = (
            ('/api/v1/tests/', settings.NUM_OBJECTS_ON_PAGE),
            (
                '/api/v1/tests/?page=2',
                settings.NUM_OBJECTS_ON_LAST_PAGE_FOR_TEST,
            ),
        )
        for url, num_object in urls_num_objects:
            with self.subTest(url=url, num_object=num_object):
                self.assertEqual(
                    len(self.authorized_user.get(url).json()['results']),
                    num_object,
                )
