import json


def load_posts():
    """Возвращает все посты"""
    with open("posts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_comments():
    """Возвращает все комментарии"""
    with open("comments.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """Функция возвращает посты определенного пользователя"""
    try:
        posts = []
        for post in load_posts():
            if post["poster_name"] == user_name:
                posts.append(post)
        return posts
    except ValueError:
        return ("пользователя нет")
    except:
        return []


def get_comments_by_post_id(post_id):
    """Функция возвращает комментарии определенного id"""
    try:
        comments = []
        for comment in load_comments():
            if comment["post_id"] == post_id:
                comments.append(comment)
        return comments
    except ValueError:
        return ("такого поста нет")
    except:
        return []


def search_for_posts(query):
    """Функция возвращает список постов по ключевому слову """
    result = []
    for post in load_posts():
        if query.lower() in post["content"].lower():
            result.append(post)
    return result


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    try:
        for post in load_posts():
            if post["pk"] == pk:
                return post
    except ValueError:
        return ("такого поста нет")

