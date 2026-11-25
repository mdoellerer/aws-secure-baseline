from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Item


class HealthEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"status": "ok"})


class ItemEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_and_retrieve_item(self):
        response = self.client.post("/api/items/", {"name": "first", "description": "demo"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        item_id = response.json()["id"]

        response = self.client.get(f"/api/items/{item_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], "first")
        self.assertEqual(Item.objects.count(), 1)

    def test_update_item(self):
        item = Item.objects.create(name="before")
        response = self.client.patch(f"/api/items/{item.pk}/", {"name": "after"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item.refresh_from_db()
        self.assertEqual(item.name, "after")

    def test_delete_item(self):
        item = Item.objects.create(name="doomed")
        response = self.client.delete(f"/api/items/{item.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)
