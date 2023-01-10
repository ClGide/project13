import pytest
from django.urls import reverse

from .models import Letting, Address


@pytest.mark.django_db
@pytest.fixture
def fill_letting_db():
    first_test_address = Address.objects.create(
        number=7217,
        street='Bedford Street',
        city='Brunswick',
        state='GA',
        zip_code=31525,
        country_iso_code='USA'
    )
    first_test_address.save()
    first_test_letting = Letting.objects.create(
        title='Joshua Tree Green Haus /w Hot Tub',
        address=first_test_address
    )
    first_test_letting.save()

    second_test_address = Address.objects.create(
        number=4,
        street='Military Street',
        city='Willoughby',
        state='OH',
        zip_code=44094,
        country_iso_code='USA'
    )
    second_test_address.save()
    second_test_letting = Letting.objects.create(
        title='Oceanview Retreat',
        address=second_test_address
    )
    second_test_letting.save()


@pytest.mark.django_db
def test_letting_index(client):
    url = reverse("oc_lettings_site.lettings:index")
    response = client.get(url)
    assert b"Letting" in response.content


letting_id_title = [
    (1, b"Joshua Tree Green Haus /w Hot Tub"),
    (2, b"Oceanview Retreat")
]


@pytest.mark.django_db
@pytest.mark.parametrize("letting_id, title", letting_id_title)
def test_letting(fill_letting_db, client, letting_id, title):
    url = reverse("oc_lettings_site.lettings:letting", kwargs={"letting_id": letting_id})
    response = client.get(url)
    assert title in response.content


