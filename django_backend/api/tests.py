from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class HealthTests(APITestCase):
    def test_health(self):
        url = reverse('Health')  # Make sure the URL is named
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Server is up!"})


class NotesCrudTests(APITestCase):
    def test_create_list_retrieve_update_delete(self):
        # List empty
        list_url = reverse('notes-list-create')
        res = self.client.get(list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json(), [])

        # Create
        payload = {"title": "Test", "content": "Body"}
        res = self.client.post(list_url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        note_id = res.json()["id"]

        # Retrieve
        detail_url = reverse('notes-detail', args=[note_id])
        res = self.client.get(detail_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()["title"], "Test")

        # Update
        res = self.client.patch(detail_url, {"title": "Test 2"}, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()["title"], "Test 2")

        # Delete
        res = self.client.delete(detail_url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        # Not found afterwards
        res = self.client.get(detail_url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
