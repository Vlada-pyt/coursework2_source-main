import logging

from flask import Flask, jsonify

from main_bp.views import main_blueprint
from utils import load_posts, get_post_by_pk

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)

logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s,[%(levelname)s], %(message)s")


@app.route("/api/posts")
def get_json():
    logging.info("Выполняю вывод всех постов")
    posts = load_posts()
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>")
def get_json_post(post_id):
    logging.info("Выполняю вывод поста по id")
    post = get_post_by_pk(post_id)
    return jsonify(post)




app.run()