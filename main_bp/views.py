from json import JSONDecodeError
import logging


from flask import Blueprint, render_template, request, jsonify

from utils import get_post_by_pk, get_comments_by_post_id, search_for_posts, load_posts, get_posts_by_user

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    try:
        post = get_post_by_pk(post_id)
        comments = get_comments_by_post_id(post_id)
    except ValueError:
        return "Введено некорректное значение"
    return render_template("post.html", post=post, comments=comments)



@main_blueprint.route("/search/")
def search_page():
    query = request.args.get("s", "")
    logging.info("Выполняю поиск")
    try:
        posts = search_for_posts(query)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template("search.html", query=query, posts=posts)


@main_blueprint.route("/users/<username>")
def get_posts_by_username(username):
    try:
        posts = get_posts_by_user(username)
    except NameError:
        return "status-code 404"
    except:
        return "Internal Server Error, status-code 500"
    return render_template("user-feed.html", posts=posts)


@main_blueprint.route("/api/posts")
def get_json():
    logging.info("Выполняю вывод всех постов")
    posts = load_posts()
    return jsonify(posts)


@main_blueprint.route("/api/posts/<int:post_id>")
def get_json_post(post_id):
    logging.info("Выполняю вывод поста по id")
    post = get_post_by_pk(post_id)
    return jsonify(post)
