import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_view(client):
    url = reverse("welcome")
    response = client.get(url)
    assert b"Welcome to Holiday Homes" in response.content

