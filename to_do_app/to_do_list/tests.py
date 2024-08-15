from django.test import TestCase
from http import HTTPStatus
from django.contrib.auth import get_user_model
from users.models import User


class RegistrationViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Philipp',
            'last_name': 'Balobanov',
            'username': 'ganjubas',
            'email': 'balobanov228@gmail.com',
            'password1': 'Maksim2004',
            'password2': 'Maksim2004',
        }

    def test_registration(self):
        response = self.client.get('/registration/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('Регистрация', response.content.decode())

    def test_user_registration_post_success(self):
        username = self.data['username']
        response = self.client.post('/registration/', self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(User.objects.filter(username=username).exists(), "Пользователь не был создан.")


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('Авторизация', response.content.decode())

    def test_user_authorization(self):
        login_success = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login_success, "Пользователь не смог войти")
        response = self.client.get('/tasks/')
        self.assertIn('Мои задачи', response.content.decode())
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_user_authorization_failed(self):
        login_failed = self.client.login(username='sdsffd', password='jedjdhd')
        self.assertFalse(login_failed, "Пользователь смог войти с неправильными данными")



