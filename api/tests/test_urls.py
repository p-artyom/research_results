from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework.test import APIClient

User = get_user_model()


class UrlsTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = mixer.blend(User)

        cls.tests = mixer.blend('researches.Test')

        cls.email = 'guido@mail.ru'
        cls.username = 'guido'
        cls.unknown_username = 'rossum'
        cls.password = 'GuidoRossum'
        cls.new_password = 'RossumGuido'

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.authorized_user = APIClient()
        cls.authorized_guido = APIClient()

        cls.authorized_user.force_authenticate(cls.user)

        cls.urls = {
            'tests': '/api/v1/tests/',
            'test': f'/api/v1/tests/{cls.tests.id}/',
            'unknown_test': '/api/v1/tests/99/',
            'users': '/auth/users/',
            'user': f'/auth/users/{cls.user.id}/',
            'unknown_user': '/auth/users/99/',
            'create': '/auth/jwt/create/',
            'password': '/auth/users/set_password/',
        }

    def test_http_statuses_get_request(self) -> None:
        """URL-адрес возвращает соответствующий статус при GET запросах."""

        urls_statuses_users = (
            (self.urls.get('tests'), HTTPStatus.UNAUTHORIZED, self.client),
            (self.urls.get('tests'), HTTPStatus.OK, self.authorized_user),
            (self.urls.get('test'), HTTPStatus.UNAUTHORIZED, self.client),
            (self.urls.get('test'), HTTPStatus.OK, self.authorized_user),
            (
                self.urls.get('unknown_test'),
                HTTPStatus.UNAUTHORIZED,
                self.client,
            ),
            (
                self.urls.get('unknown_test'),
                HTTPStatus.NOT_FOUND,
                self.authorized_user,
            ),
            (self.urls.get('user'), HTTPStatus.UNAUTHORIZED, self.client),
            (self.urls.get('user'), HTTPStatus.OK, self.authorized_user),
            (
                self.urls.get('unknown_user'),
                HTTPStatus.UNAUTHORIZED,
                self.client,
            ),
            (
                self.urls.get('unknown_user'),
                HTTPStatus.NOT_FOUND,
                self.authorized_user,
            ),
        )
        for url, status, user in urls_statuses_users:
            with self.subTest(url=url, status=status, user=user):
                self.assertEqual(user.get(url).status_code, status)

    def test_http_statuses_post_request(self) -> None:
        """URL-адрес возвращает корректный статус.

        Статус, возвращаемый при POST и DELETE запросах на URL-адреса,
        соответствует документации.
        """

        urls_statuses_users_data = (
            (
                self.urls.get('users'),
                HTTPStatus.CREATED,
                self.client,
                {
                    'email': self.email,
                    'username': self.username,
                    'password': self.password,
                },
            ),
            (
                self.urls.get('users'),
                HTTPStatus.BAD_REQUEST,
                self.client,
                {
                    'email': self.email,
                    'username': self.username,
                    'password': self.password,
                },
            ),
            (
                self.urls.get('create'),
                HTTPStatus.OK,
                self.client,
                {
                    'username': self.username,
                    'password': self.password,
                },
            ),
            (
                self.urls.get('create'),
                HTTPStatus.BAD_REQUEST,
                self.client,
                {
                    'email': self.unknown_username,
                    'password': self.password,
                },
            ),
        )
        for url, status, user, data in urls_statuses_users_data:
            with self.subTest(url=url, status=status, user=user):
                self.assertEqual(
                    user.post(url, data=data, format='json').status_code,
                    status,
                )
        guido = User.objects.get(username=self.username)
        self.authorized_guido.force_authenticate(user=guido)
        urls_statuses_users_data = (
            (
                self.urls.get('password'),
                HTTPStatus.NO_CONTENT,
                self.authorized_guido,
                {
                    'new_password': self.new_password,
                    'current_password': self.password,
                },
            ),
            (
                self.urls.get('password'),
                HTTPStatus.BAD_REQUEST,
                self.authorized_guido,
                {
                    'new_passworddd': self.new_password,
                    'current_passworddd': self.password,
                },
            ),
            (
                self.urls.get('password'),
                HTTPStatus.UNAUTHORIZED,
                self.client,
                {},
            ),
        )
        for url, status, user, data in urls_statuses_users_data:
            with self.subTest(url=url, status=status, user=user):
                self.assertEqual(
                    user.post(url, data=data, format='json').status_code,
                    status,
                )
