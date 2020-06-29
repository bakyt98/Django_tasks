from django.test import TestCase, RequestFactory
from . import views
from model_mommy import mommy
from .models import Car, MainUser
from .token import get_token



class MainUserApiTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_create_user(self):
        data = {
            "username": "isimovabakyt",
            'email': "a@a.com",
            "full_name": "test test",
            "password": "a"
        }
        request = self.factory.post('create_user', data=data)
        response = views.create_user(request)
        self.assertEqual(response.data['user']['username'], data['username'])
        self.assertEqual(response.data['user']['email'], data['email'])
        self.assertEqual(response.data['user']['full_name'], data['full_name'])


class CarApiTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = momy.make(MainUser)
        self.token = get_token(self.user)
        car = mommy.make(Car, name="BMW")

    def test_get_cars(self):
        auth_headers = {
            "HTTP_AUTHORIZATION": f"JWT {self.token}"
        }
        request = self.factory('cars', **auth_headers)
        response = views.CarViewSet(request)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].name, "BMW")
