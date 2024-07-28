from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Review
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.book = Book.objects.create(
            title="Test Book1",
            author="Test Author1",
            publication_date="2024-07-26",
            genre="Function",
            description="Test Description"
        )

    def test_create_book(self):
        url = reverse('book-list-create')
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_date": "2024-07-26",
            "genre": "Non-Function",
            "description": "New Description"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books(self):
        url = reverse('book-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "publication_date": "2024-07-",
            "genre": "Updated Genre",
            "description": "Updated Description"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_review(self):
        url = reverse('review-list-create', args=[self.book.id])
        data = {
            "review": "Test Review",
            "rating": 5,
            "reviewer": "Test Reviewer"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reviews(self):
        url = reverse('review-list-create', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_summary(self):
        url = reverse('book-summary', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

