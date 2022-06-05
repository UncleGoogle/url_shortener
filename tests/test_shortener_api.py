"""
Some tests here run on details parametrization which is more appropriate on unit level
This have to be refactored after the project goes bigger and leaves POC state.
For now, playing with db does not hurt.
"""

import json

import pytest


pytestmark = pytest.mark.django_db


@pytest.mark.parametrize("url", [
    "noturl",
    "www.forget-schema.com",
])
def test_create_alias_with_malformed_url(api_client, url):
    data = {
        "url": url,
        "alias": "an_alias",
    }

    response = api_client().post("/shorten/", data=data, format='json')

    assert response.status_code == 400


def test_create_alias_when_it_is_already_taken(api_client):
    for url in ["http://one.com", "http://two.com"]:
        response = api_client().post(
            "/shorten/",
            data={"url": url, "alias": "the_same"},
            format='json'
        )
    
    assert response.status_code == 400, response.content
    assert b"already exists" in response.content


@pytest.mark.parametrize("url", [
    "https://google.com",
    "https://www.goo.com",
    "http://www.goo.com",
    "http://點看.cn",
    pytest.param("https%3A%2F%2Fwww.punycoder.com%2F", marks=pytest.mark.xfail(reason="no support for quoted links yet"))
])
def test_create_alias_for_correct_input(api_client, url):
    data = {
        "url": url,
        "alias": "UncleGoogle",
    }

    response = api_client().post("/shorten/", data=data, format='json')
    
    assert response.status_code == 201, response.content
    assert json.loads(response.content) == data


def test_get_not_existing_alias(api_client):
    response = api_client().get("/shorten/non_existing_one")

    assert response.status_code == 404, response.content
    assert response.content == b''


def test_create_alias_and_get_it(api_client):
    original_url = "https://www.djangoproject.com/"
    alias = "django"

    data = {
        "url": original_url,
        "alias": alias,
    }
    api_client().post("/shorten/", data=data, format='json')

    response = api_client().get(f"/shorten/{alias}")

    assert response.status_code == 200, response.content
    assert json.loads(response.content) == data
     