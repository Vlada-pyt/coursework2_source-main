import pytest

from run import app

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_app():
    response = app.test_client().get("/api/posts")

    assert response.status_code == 200, "Статус-код всех постов неверный"
    assert type(response.json) == list, "возвращается не список"
    assert set(response.json[0].keys()) == keys_should_be, "неверный список ключей"



