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

# =====USERS CREATE=====


@pytest.fixture
def create_user(db):
    user = get_user_model().objects.create_user(
        username='testuser',
        password='123'
    )
    token, _ = Token.objects.get_or_create(user=user)
    print('TOKEN', token)
    print('USER', user)
    return user, token.key


@pytest.fixture
def create_admin_user(db):
    user = get_user_model().objects.create_superuser(
        username='admin',
        password='pswd',
        email=None,
    )
    token, _ = Token.objects.get_or_create(user=user)
    return user, token

# ====ADDITIONAL CLIENTS====


@pytest.fixture
def authenticated_client(create_user):
    api_client = APIClient()
    user, token = create_user
    token_str = 'Token ' + token
    api_client.credentials(HTTP_AUTHORIZATION=token_str)
    return api_client


@pytest.fixture
def admin_client(create_admin_user):
    api_client = APIClient()
    user, token = create_admin_user
    token_str = 'Token ' + token.key
    api_client.credentials(HTTP_AUTHORIZATION=token_str)
    return api_client

# =====DATA FIXTURES=====


@pytest.fixture
def author_data():
    return {
        'book': [],
        'first_name': 'fname',
        'last_name': 'lname',
        'pen_name': 'pname',
    }


@pytest.fixture
def author_create(db):
    author = Author.objects.create(
        first_name='author',
        last_name='author',
        pen_name='author',
    )
    return author


@pytest.fixture
def author_patch_data():
    return {
        'first_name': 'new_name',
    }


@pytest.fixture
def author_patch_expected(author_create):
    return {
        'id': author_create.id,
        'first_name': 'new_name',
        'last_name': author_create.last_name,
        'pen_name': author_create.pen_name,
    }

# =============TESTS=============


def test_author_get(
    api_client,
    authenticated_client,
    admin_client,
    db,
):
    response_unauthenticated = api_client.get(reverse_lazy('author-list'))
    response_authenticated = authenticated_client.get(
        reverse_lazy('author-list')
    )
    response_admin = admin_client.get(reverse_lazy('author-list'))

    assert response_unauthenticated.status_code == 200
    assert response_authenticated.status_code == 200
    assert response_admin.status_code == 200


def test_author_create(
    api_client,
    authenticated_client,
    admin_client,
    author_data,
    db,
):
    response_unauthenticated = api_client.post(
        reverse_lazy('author-list'),
        data=author_data,
        format='json',
    )
    response_authenticated = authenticated_client.post(
        reverse_lazy('author-list'),
        data=author_data,
        format='json',
    )
    response_admin = admin_client.post(
        reverse_lazy('author-list'),
        data=author_data,
        format='json',
    )
    assert response_unauthenticated.status_code == 401
    assert response_authenticated.status_code == 403
    assert response_admin.status_code == 201


def test_author_update_put(
    api_client,
    authenticated_client,
    admin_client,
    author_create,
    author_data,
    db,
):
    response_unauthenticated = api_client.put(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id}),
        data=author_data,
        format='json',
    )
    response_authenticated = authenticated_client.put(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id}),
        data=author_data,
        format='json',
    )
    response_admin = admin_client.put(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id}),
        data=author_data,
        format='json',
    )
    assert response_unauthenticated.status_code == 401
    assert response_authenticated.status_code == 403
    assert response_admin.status_code == 200


def test_author_update_patch(
    api_client,
    authenticated_client,
    admin_client,
    author_create,
    author_patch_data,
    author_patch_expected,
):
    response_unauthenticated = api_client.patch(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id}),
        data=author_patch_data,
        format='json',
    )
    response_authenticated = authenticated_client.patch(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id}),
        data=author_patch_data,
        format='json',
    )
    response_admin = admin_client.patch(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id}),
        data=author_patch_data,
        format='json',
    )
    admin_res_actual = Author.objects.filter(
        id=author_create.id
    ).values().first()

    assert response_unauthenticated.status_code == 401
    assert response_authenticated.status_code == 403
    assert response_admin.status_code == 200
    print('ACTUAL', admin_res_actual)
    print('EXPECTED', author_patch_expected)
    assert admin_res_actual == author_patch_expected


def test_author_delete(
    api_client,
    authenticated_client,
    admin_client,
    author_create,
):
    response_unauthenicated = api_client.delete(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id})
    )
    response_authenticated = authenticated_client.delete(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id})
    )
    response_admin = admin_client.delete(
        reverse_lazy('author-detail', kwargs={'pk': author_create.id})
    )

    assert response_unauthenicated.status_code == 401
    assert response_authenticated.status_code == 403
    assert response_admin.status_code == 204
