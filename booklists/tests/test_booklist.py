from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
import pytest
from rest_framework.authtoken.models import Token


# ========PYTEST FIXTURES=========


@pytest.fixture
def create_user(db):
    user = get_user_model().objects.create_user(
        username='user',
        password='pswd',
    )
    token = Token.objects.get_or_create(user=user)
    return user, token


@pytest.fixture
def create_superuser(db):
    user = get_user_model().objects.create_superuser(
        username='admin',
        password='pswd',
        email=None,
    )
    token = Token.objects.get_or_create(user=user)
    return user, token


@pytest.fixture
def unauthenticated_client():
    return APIClient()


@pytest.fixture
def authenticated_client(create_user):
    client = APIClient()
    _, token = create_user
    token_str = 'Token ' + token
    client.credentials(
        HTTP_AUTHENTICATION=token_str
    )
    return client


@pytest.fixture
def admin_client(create_superuser):
    client = APIClient()
    _, token = create_superuser
    token_str = 'Token ' + token
    client.credentials(
        HTTP_AUTHENTICATION=token_str
    )
    return client


# =======TESTS=======


def test_booklists_get(
    unauthenticated_client,
    authenticated_client,
    admin_client,
):
    url = 'booklist-list'
    unauthenticated_response = unauthenticated_client.get(
        reverse_lazy(url)
    )
    authenticated_response = authenticated_client.get(
        reverse_lazy(url)
    )
    admin_response = admin_client.get(
        reverse_lazy(url)
    )
    
    assert unauthenticated_response.status_code == 200
    assert authenticated_response.status_code == 200
    assert admin_response.status_code == 200
