# tests.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PlacesRemember.settings')
django.setup()

# tests.py

import pytest  # noqa: E402
from django.contrib.auth.models import User  # noqa: E402
from django.shortcuts import get_object_or_404  # noqa: E402
from django.test import Client  # noqa: E402
from django.urls import reverse  # noqa: E402
from .models import Memory  # noqa: E402
from PlacesRemember.forms import MemoryForm  # noqa: E402
from allauth.socialaccount.models import SocialAccount  # noqa: E402


@pytest.fixture
def user():
    # Create a test user
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def user2():
    # Create a test user
    return User.objects.create_user(username='testuser2', password='testpass2')


@pytest.fixture
def client(user):
    # Create a test client and authenticate as the test user
    client = Client()
    client.force_login(user)
    return client


@pytest.mark.django_db
def test_welcome(client):
    response = client.get(reverse('welcome'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_home(client, user):
    client.force_login(user)

    SocialAccount.objects.create(
        user=user,
        provider='vk',
        extra_data={
            'photo_max_orig':
                'https://i.ytimg.com/vi/XZxu1kiP65w/maxresdefault.jpg'}
    )

    client.post(reverse('add_memory'), {
        'place_name': 'Test Place404',
        'comment': 'Test Comment',
        'latitude': 123.456,
        'longitude': 789.012,
        'user': user.id  # Associate the memory with the test user
    })
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert response.context[
               'profile_picture'] == \
           'https://i.ytimg.com/vi/XZxu1kiP65w/maxresdefault.jpg'
    assert response.context['memories'][0].place_name == 'Test Place404'

    # Create a Google SocialAccount for the authenticated user
    SocialAccount.objects.create(
        user=user,
        provider='google',
        extra_data={'picture': 'https://lookw.ru/9/980/1566944536-1-38.jpg'}
    )
    response = client.get(reverse('home'))
    assert response.context[
               'profile_picture'] == \
           'https://lookw.ru/9/980/1566944536-1-38.jpg'


@pytest.mark.django_db
def test_add_memory(client, user):
    # Simulate creating a new memory associated with the test user
    response = client.post(reverse('add_memory'), {
        'place_name': 'Test Place',
        'comment': 'Test Comment',
        'latitude': 123.456,
        'longitude': 789.012,
        'user': user.id  # Associate the memory with the test user
    })
    assert response.status_code == 302

    # Check if the user is redirected to the correct location
    assert response.url == reverse('home')

    # Verify that the memory is created in the database
    assert Memory.objects.filter(place_name='Test Place',
                                 comment='Test Comment',
                                 user=user).exists()

    response = client.get(reverse('add_memory'))
    assert isinstance(response.context['form'], MemoryForm)


@pytest.mark.django_db
def test_display_memory(client, user):
    # Create a memory
    memory = Memory.objects.create(
        place_name='Test Place',
        comment='Test Comment',
        latitude=123.456,
        longitude=789.012,
        user=user
    )

    # Retrieve the memory
    response = client.get(reverse('display_memory', args=[memory.id]))

    assert response.status_code == 200

    # Check if the memory details are present in the response
    form = response.context['form']
    # Compare form widget contents with memory values
    rendered_form = form.as_table()

    assert str(memory.place_name) in rendered_form
    assert str(memory.comment) in rendered_form
    assert str(memory.latitude) in rendered_form
    assert str(memory.longitude) in rendered_form

    response = client.post(reverse('display_memory', args=[memory.id]), {
        'place_name': 'Changed Test Place',
        'comment': 'Changed Test Comment',
        'latitude': 456.123,
        'longitude': 012.789,
        'user': user.id  # Associate the memory with the test user
    })
    assert response.status_code == 302
    assert response.url == reverse('home')

    changedMemory = get_object_or_404(Memory, id=memory.id)

    assert changedMemory.place_name == 'Changed Test Place'
    assert changedMemory.comment == 'Changed Test Comment'
    assert changedMemory.latitude == 456.123
    assert changedMemory.longitude == 012.789


@pytest.mark.django_db
def test_retrieve_memories_for_user(client, user, user2):
    Memory.objects.create(
        place_name='Test Place 1',
        comment='Test Comment 1',
        latitude=123.456,
        longitude=789.012,
        user=user
    )
    Memory.objects.create(
        place_name='Test Place 2',
        comment='Test Comment 2',
        latitude=1.456,
        longitude=1.012,
        user=user
    )
    memory3 = Memory.objects.create(
        place_name='Test Place user2 1',
        comment='Test Comment user2 1',
        latitude=5.456,
        longitude=6.012,
        user=user2
    )
    memory4 = Memory.objects.create(
        place_name='Test Place user2 2',
        comment='Test Comment user2 2',
        latitude=7.456,
        longitude=8.012,
        user=user2
    )
    mems = list(Memory.objects.filter(user=user2))
    assert mems == [memory3, memory4]
