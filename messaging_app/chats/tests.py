from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class SmokeTests(TestCase):
    """Very small smoke tests to ensure endpoints are wired."""

    def setUp(self):
        self.client = APIClient()

    def test_list_conversations(self):
        url = reverse('conversation-list')
        resp = self.client.get(url)
        # should return 200 (may be empty list)
        self.assertIn(resp.status_code, (status.HTTP_200_OK, status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED))

    def test_list_messages(self):
        url = reverse('message-list')
        resp = self.client.get(url)
        self.assertIn(resp.status_code, (status.HTTP_200_OK, status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED))
