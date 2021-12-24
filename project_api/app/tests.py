import requests
from django.test import TestCase, Client
from django.urls import reverse
from .views import get_data_from_url


class TestCsv(TestCase):

    def setUp(self):
        self.client = Client()
        self.csv_reverse = reverse('csv_output')

    def test_csv_status_code(self):
        response = self.client.get(self.csv_reverse)
        self.assertEquals(response.status_code, 200)


class TestScrapingData(TestCase):

    def test_get_data_from_url(self):
        self.assertEquals(get_data_from_url('users'),
                          requests.get('https://jsonplaceholder.typicode.com/users').json())
        self.assertEquals(get_data_from_url('todos'),
                          requests.get('https://jsonplaceholder.typicode.com/todos').json())
        self.assertIsNone(get_data_from_url('todo'))
        self.assertIsNone(get_data_from_url('tasks'))
        self.assertIsNone(get_data_from_url('user'))
        self.assertIsNone(get_data_from_url())
        self.assertIsNone(get_data_from_url(1))

