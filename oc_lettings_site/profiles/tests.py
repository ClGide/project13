import pytest
from django.urls import reverse

from .models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
@pytest.fixture
def fill_profile_db():
    first_test_user = User.objects.create(
        password=7217902838,
        username='HeadlinesGazer',
        first_name='Jamie',
        last_name='Lal',
        email='jssssss33@acee9.live'
    )
    first_test_user.save()
    first_test_profile = Profile.objects.create(
        user=first_test_user,
        favorite_city="Buenos Aires"
    )
    first_test_profile.save()

    second_test_user = User.objects.create(
        password=727273898,
        username='DavWin',
        first_name='Cassandra',
        last_name='Grahm',
        email='5houssam.kessaiso@facpidif.ml'
    )
    second_test_user.save()
    second_test_profile = Profile.objects.create(
        user=second_test_user,
        favorite_city="Barcelona"
    )
    second_test_profile.save()


@pytest.mark.django_db
def test_profile_index(client):
    url = reverse("oc_lettings_site.profiles:index")
    response = client.get(url)
    assert b"Profiles" in response.content


username_title = [
    ("HeadlinesGazer", b"HeadlinesGazer"),
    ("DavWin", b"DavWin")
]


@pytest.mark.django_db
@pytest.mark.parametrize("username, title", username_title)
def test_profile(fill_profile_db, client, username, title):
    url = reverse("oc_lettings_site.profiles:profile", kwargs={"username": username})
    response = client.get(url)
    assert title in response.content


