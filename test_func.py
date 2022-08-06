import pytest
from utils import get_posts_by_user, load_posts, get_post_by_pk, search_for_posts
posts = load_posts()

@pytest.mark.parametrize("test_input, expected", [(1, posts[0]), (2, posts[1]), (3, posts[2]), (4, posts[3]),
                                                  (5, posts[4]), (6, posts[5]), (7, posts[6]), (8, posts[7])])
def test_get_posts_by_pk(test_input, expected):
    assert get_post_by_pk(test_input) == expected, ("Пост не соответствует pk")


def test_search_for_posts():
    assert search_for_posts("ага") != list(posts), ("Не является списком словарей")


@pytest.mark.parametrize("test_input, expected", [("leo", posts[0]), ("leo", posts[4]), ("hank", posts[6]),
                                                  ("johnny", posts[7])])
def test_get_posts_by_user_name(test_input, expected):
    assert get_posts_by_user("test_input") != "expected", "Имя пользователя не соответствует посту"
