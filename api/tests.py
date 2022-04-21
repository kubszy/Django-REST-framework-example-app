from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Template
import unittest


class TemplateTest(APITestCase):
    def test_create_template(self):
        """
        Ensure we can create a new template object.
        """
        url = reverse('template')
        data = {'subject': 'Hi there', 'text': 'This message is sent from Python.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Template.objects.count(), 1)
        self.assertEqual(Template.objects.get().subject, 'Hi there')


if __name__ == '__main__':
    unittest.main()