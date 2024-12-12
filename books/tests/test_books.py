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
    user = get_user_model().objects.create_user(
        username='testuser',
        password='123'
    )
    token, _ = Token.objects.get_or_create(user=user)
    # print('TOKEN', token)
    # print('USER', user)
    return user, token.key


@pytest.fixture
def create_another_user(db):
    user = get_user_model().objects.create_user(
        username='another-test-user',
        password='1234',
    )
    token, _ = Token.objects.get_or_create(user=user)
    return user, token.key


@pytest.fixture
def create_superuser(db):
    user = get_user_model().objects.create_superuser(
        username='admin',
        password='pswd',
        email=None,
    )
    token, _ = Token.objects.get_or_create(user=user)
    return user, token

# ========PYTEST FIXTURES=========
# ========CLIENTS========


@pytest.fixture
def unauthenticated_client():
    return APIClient()


@pytest.fixture
def authenticated_client(create_user):
    api_client = APIClient()
    user, token = create_user
    token_str = 'Token ' + token
    api_client.credentials(HTTP_AUTHORIZATION=token_str)
    return api_client


@pytest.fixture
def another_authenticated_client(create_another_user):
    api_client = APIClient()
    user, token = create_another_user
    token_str = 'Token ' + token
    api_client.credentials(HTTP_AUTHORIZATION=token_str)
    return api_client


@pytest.fixture
def admin_client(create_superuser):
    api_client = APIClient()
    user, token = create_superuser
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
def book_patch_data():
    return {
        'name': 'new_name',
    }


@pytest.fixture
def book_patch_expected(book_create):
    return {
        'id': book_create.id,
        'name': 'new_name',
        'description': 'sdf',
    }


@pytest.fixture
def book_data(create_author):
    author_url = reverse_lazy('author-detail', kwargs={'pk': create_author.id})
    return {
        'name': 'testbook',
        'description': 'testdesc',
        'author': [author_url],
    }
# =======TESTS=======


def test_books_get(
    unauthenticated_client,
    authenticated_client,
    admin_client,
):
    url = 'book-list'
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


def test_books_create(
    unauthenticated_client,
    authenticated_client,
    admin_client,
    book_data,
):
    url = 'book-list'
    response_unauthenticated = unauthenticated_client.post(
        reverse_lazy(url),
        data=book_data,
        format='json',
    )
    response_authenticated = authenticated_client.post(
        reverse_lazy(url),
        data=book_data,
        format='json',
    )
    response_admin = admin_client.post(
        reverse_lazy(url),
        data=book_data,
        format='json',
    )
    print('RESPADM///////////////////////////////', response_admin.data)

    assert response_unauthenticated.status_code == 401
    assert response_authenticated.status_code == 403
    assert response_admin.status_code == 201


def test_books_update_put(
    unauthenticated_client,
    authenticated_client,
    another_authenticated_client,
    admin_client,
    book_create,
    book_data,
    db,
):
    url = 'book-detail'

    response_unauthenticated = unauthenticated_client.put(
        reverse_lazy(url, kwargs={'pk': book_create.id}),
        data=book_data,
        format='json',
    )
    response_authenticated_owner = authenticated_client.put(
        reverse_lazy(url, kwargs={'pk': book_create.id}),
        data=book_data,
        format='json',
    )
    response_authenticated = another_authenticated_client.put(
        reverse_lazy(url, kwargs={'pk': book_create.id}),
        data=book_data,
        format='json',
    )
    response_admin = admin_client.put(
        reverse_lazy(url, kwargs={'pk': book_create.id}),
        data=book_data,
        format='json',
    )

    assert response_unauthenticated.status_code == 401
    assert response_authenticated_owner.status_code == 403
    assert response_authenticated.status_code == 403
    assert response_admin.status_code == 200


def test_books_update_patch(
    unauthenticated_client,
    authenticated_client,
    another_authenticated_client,
    admin_client,
    book_create,
    book_patch_data,
    book_patch_expected,
):
    url = 'book-detail'
    response_unauthenticated = unauthenticated_client.patch(
        reverse_lazy(url, kwargs={'pk': book_create.id}),
        data=book_patch_data,
        format='json',
    )
    response_authenticated_owner = authenticated_client.patch(
        reverse_lazy(url, kwargs={'pk': book_create.id}),
        data=book_patch_data,
        format='json',
    )
    response_authenticated = another_authenticated_client.patch(
        reverse_lazy(url, kwargs={'pk': book_create.id}),
        data=book_patch_data,
        format='json',
    )
    response_admin = admin_client.patch(
        reverse_lazy(url, kwargs={'pk': book_create.id}),
        data=book_patch_data,
        format='json',
    )
    res_actual = Book.objects.filter(
        id=book_create.id
    ).values().first()

    assert response_unauthenticated.status_code == 401
    assert response_authenticated_owner.status_code == 403
    assert response_authenticated.status_code == 403
    assert response_admin.status_code == 200
    assert res_actual == book_patch_expected


def test_books_delete(
    unauthenticated_client,
    authenticated_client,
    another_authenticated_client,
    admin_client,
    book_create,
):
    url = 'book-detail'
    response_unauthenicated = unauthenticated_client.delete(
        reverse_lazy(url, kwargs={'pk': book_create.id})
    )
    response_authenticated = another_authenticated_client.delete(
        reverse_lazy(url, kwargs={'pk': book_create.id})
    )
    response_admin = admin_client.delete(
        reverse_lazy(url, kwargs={'pk': book_create.id})
    )
    response_authenticated_owner = authenticated_client.delete(
        reverse_lazy(url, kwargs={'pk': book_create.id})
    )

    assert response_unauthenicated.status_code == 401
    assert response_authenticated.status_code == 403
    assert response_authenticated_owner.status_code == 403
    assert response_admin.status_code == 204
