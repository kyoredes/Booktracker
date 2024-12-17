from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
import pytest
from books.models import Book
from authors.models import Author
from rest_framework.authtoken.models import Token
from booklists.models import Booklist


# ========PYTEST FIXTURES=========
# ========USERS========
@pytest.fixture
def create_user(db):
    pswd = '123'
    user = get_user_model().objects.create_user(
        username='testuser',
        password=pswd
    )
    token, _ = Token.objects.get_or_create(user=user)
    return user, token.key, pswd


@pytest.fixture
def create_another_user(db):
    pswd = '1234'
    user = get_user_model().objects.create_user(
        username='another-test-user',
        password=pswd,
    )
    token, _ = Token.objects.get_or_create(user=user)
    return user, token.key, pswd


@pytest.fixture
def create_superuser(db):
    pswd = 'pswd'
    user = get_user_model().objects.create_superuser(
        username='admin',
        password=pswd,
        email=None,
    )
    token, _ = Token.objects.get_or_create(user=user)
    return user, token, pswd

# ========PYTEST FIXTURES=========
# ========CLIENTS========


@pytest.fixture
def unauthenticated_client():
    return APIClient()


@pytest.fixture
def authenticated_client(create_user):
    api_client = APIClient()
    user, token, _ = create_user
    token_str = 'Token ' + token
    print('TOKEn///////////////////////////////////', token_str)
    api_client.credentials(HTTP_AUTHORIZATION=token_str)
    return api_client


@pytest.fixture
def another_authenticated_client(create_another_user):
    api_client = APIClient()
    user, token, _ = create_another_user
    token_str = 'Token ' + token
    api_client.credentials(HTTP_AUTHORIZATION=token_str)
    return api_client


@pytest.fixture
def admin_client(create_superuser):
    api_client = APIClient()
    user, token, _ = create_superuser
    token_str = 'Token ' + token.key
    api_client.credentials(HTTP_AUTHORIZATION=token_str)
    return api_client

# ========PYTEST FIXTURES=========
# ========OBJECTS========


@pytest.fixture
def create_author(db):
    return Author.objects.create(
        first_name='sdf',
        last_name='sd',
        pen_name='dsf',
    )


@pytest.fixture
def book_create(db, create_author):
    book = Book.objects.create(
        id=1,
        name='name',
        description='sdf',
    )
    book.author.set([create_author])
    return book

# ========PYTEST FIXTURES=========
# ========DATA========


@pytest.fixture
def user_patch_data():
    return {
        'username': 'new_name',
    }


@pytest.fixture
def user_patch_expected(create_user):
    return {
        'id': create_user[0].id,
        'username': 'new_name',
    }


@pytest.fixture
def user_data():
    return {
        'username': '1234',
        'password': '123',
    }
# =======TESTS=======


def test_users_get(
    unauthenticated_client,
    authenticated_client,
    admin_client,
):
    url = 'customuser-list'
    response_unauthenticated = unauthenticated_client.get(
        reverse_lazy(url)
    )
    response_authenticated = authenticated_client.get(
        reverse_lazy(url)
    )
    response_admin = admin_client.get(
        reverse_lazy(url)
    )

    assert response_unauthenticated.status_code == 401
    assert response_authenticated.status_code == 200
    assert response_admin.status_code == 200


def test_users_create_unauth(
    unauthenticated_client,
    user_data,
    db,
):
    url = 'customuser-list'
    response_unauthenticated = unauthenticated_client.post(
        reverse_lazy(url),
        data=user_data,
        format='json',
    )
    assert response_unauthenticated.status_code == 201


def test_users_create_auth(
    authenticated_client,
    user_data,
    db,
):
    url = 'customuser-list'
    response_authenticated = authenticated_client.post(
        reverse_lazy(url),
        data=user_data,
        format='json',
    )
    assert response_authenticated.status_code == 201


def test_user_create_admin(
    admin_client,
    user_data,
    db,
):
    url = 'customuser-list'
    response_admin = admin_client.post(
        reverse_lazy(url),
        data=user_data,
        format='json',
    )
    assert response_admin.status_code == 201


def test_users_update_put_unauth(
    unauthenticated_client,
    create_user,
    user_data,
    db
):
    url = 'customuser-detail'
    response_unauthenticated = unauthenticated_client.put(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data=user_data,
        format='json',
    )
    assert response_unauthenticated.status_code == 401


def test_users_update_put_auth(
    authenticated_client,
    another_authenticated_client,
    create_another_user,
    user_data,
    db,
):
    url = 'customuser-detail'
    response_authenticated = another_authenticated_client.put(
        reverse_lazy(url, kwargs={'id': create_another_user[0].id}),
        data=user_data,
        format='json',
    )

    assert response_authenticated.status_code == 200


def test_users_update_put_auth_owner(
    authenticated_client,
    create_user,
    user_data,
    db,
):
    url = 'customuser-detail'
    response_authenticated_owner = authenticated_client.put(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data=user_data,
        format='json',
    )
    assert response_authenticated_owner.status_code == 200


def test_users_update_put_admin(
    admin_client,
    user_data,
    create_user
):
    url = 'customuser-detail'
    response_admin = admin_client.put(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data=user_data,
        format='json',
    )
    assert response_admin.status_code == 200


def test_users_update_patch(
    unauthenticated_client,
    authenticated_client,
    another_authenticated_client,
    admin_client,
    create_user,
    user_patch_data,
    user_patch_expected,
):
    url = 'customuser-detail'
    response_unauthenticated = unauthenticated_client.patch(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data=user_patch_data,
        format='json',
    )
    response_authenticated_owner = authenticated_client.patch(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data=user_patch_data,
        format='json',
    )
    response_authenticated = another_authenticated_client.patch(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data=user_patch_data,
        format='json',
    )
    response_admin = admin_client.patch(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data=user_patch_data,
        format='json',
    )
    res_actual = get_user_model().objects.filter(
        id=create_user[0].id
    ).values().first()

    assert response_unauthenticated.status_code == 401
    assert response_authenticated.status_code == 404
    assert response_authenticated_owner.status_code == 200
    assert response_admin.status_code == 200
    assert res_actual['id'] == user_patch_expected['id']
    assert res_actual['username'] == user_patch_expected['username']


def test_users_delete(
    unauthenticated_client,
    authenticated_client,
    another_authenticated_client,
    admin_client,
    create_user,
    create_another_user,
    create_superuser
):
    url = 'customuser-detail'
    response_unauthenicated = unauthenticated_client.delete(
        reverse_lazy(url, kwargs={'id': create_user[0].id})
    )
    response_authenticated = another_authenticated_client.delete(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data={'current_password': create_another_user[2]}
    )

    response_authenticated_owner = authenticated_client.delete(
        reverse_lazy(url, kwargs={'id': create_user[0].id}),
        data={'current_password': create_user[2]}
    )
    response_admin = admin_client.delete(
        reverse_lazy(url, kwargs={'id': create_another_user[0].id}),
        data={'current_password': create_superuser[2]}
    )
    assert response_unauthenicated.status_code == 401
    print('//////////////////', response_authenticated.data)
    assert response_authenticated.status_code == 403
    print('OWNER////////', response_authenticated_owner.data)
    assert response_authenticated_owner.status_code == 204
    print(response_admin.data)
    assert response_admin.status_code == 204
