from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from rest_framework import status
from authors.models import Author


class APIUrlsTest(APITestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Author first name',
            'last_name': 'Author last name',
            'pen_name': 'Pen name',
        }
        self.model_object = Author.objects.create(**self.data)
        self.id = self.model_object.get('id')

    def test_author_get(self):
        response = self.client.get(reverse_lazy('author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_author_post(self):
        response = self.client.post(
            reverse_lazy('author-list'),
            data=self.data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 1)

    def test_author_get_detail(self):
        response = self.client.get(
            reverse_lazy('author-detail', kwargs={'pk': self.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_author_patch_detail(self):
        id = self.client.patch(
            reverse_lazy('author-detail', kwargs={'pk': self.id}),
            data={'first_name': 'New first name'},
            format='json',
        ).data['id']
        new_data = self.data['first_name'] = 'New first name'
        response = self.client.get(
            reverse_lazy('author-detail', kwargs={'pk': id}),
        )
        self.assertEqual(response.data, new_data)

    def test_author_put_detail(self):
        id = self.client.patch(
            reverse_lazy('author-detail', kwargs={'pk': self.id}),
            data={'first_name': 'New first name'},
            format='json',
        ).data['id']
        new_data = self.data['first_name'] = 'New first name'
        response = self.client.get(
            reverse_lazy('author-detail', kwargs={'pk': id}),
        )
        self.assertEqual(response.data, new_data)
