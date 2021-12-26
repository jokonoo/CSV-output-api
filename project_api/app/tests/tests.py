import requests
from django.test import TestCase, Client
from django.urls import reverse
from ..api_data_scraper import get_data_from_url
from ..api_data_scraper import api_get_user_data, api_get_task_data


class TestCsv(TestCase):

    def setUp(self):
        self.client = Client()
        self.csv_reverse = reverse('csv_output')
        self.response = self.client.get(self.csv_reverse)

    def test_csv_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_csv_response_type(self):
        self.assertEquals(self.response.get('Content-Disposition'),
                          "attachment; filename=users_tasks.csv")

    def test_csv_response_content(self):
        with open('app/tests/test_csv.csv', 'rb') as test_file:
            self.assertEquals(self.response.content, test_file.read())



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

    def test_api_get_user_data(self):
        self.assertIsNone(api_get_user_data())
        self.assertIsNone(api_get_task_data())

