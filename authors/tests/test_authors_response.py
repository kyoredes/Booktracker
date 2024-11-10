import pytest
from rest_framework.test import APIClient
from django.urls import reverse_lazy
from authors.models import Author
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# =============FIXTURES=============
@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def get_author_object(db):
    return Author.objects.create(
        first_name='Firstname',
        last_name='Lastname',
        pen_name='Penname',
    )


@pytest.fixture
def create_user(db):
    user = get_user_model().objects.create(
        username='testuser'
    )
    token, _ = Token.objects.get_or_create(user=user)
    print('TOKEN', token)
    print('TOKEN 2', token.key)
    return user, token.key


@pytest.fixture
def authenticated_client(api_client, create_user):
    user, token = create_user
    token_str = 'Token ' + token
    api_client.credentials(HTTP_AUTHORIZATION=token_str)
    return api_client

# =============TESTS=============


def test_author_get_unauthenticated(api_client):
    response = api_client.get(reverse_lazy('authors-list'))
    assert response.status_code == 200


def test_author_get_authenticated(authenticated_client):
    response = authenticated_client.get(reverse_lazy('authors-list'))
    assert response.status_code == 200
