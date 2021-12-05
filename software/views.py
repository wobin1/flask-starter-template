from flask import Blueprint, request,json, jsonify
from .models import Post
from software import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return 'hello world'


@views.route('/create_post', methods=["GET", "POST"])
def create_post():
    if request.method =="POST":
        title = request.form["title"]
        post = request.form["content"]
        author = request.form["author"]

        create_post = Post(title=title, content=post, author=author)

        db.session.add(create_post)
        db.session.commit()
           
        return jsonify(["Register success"])


@views.route('/post', methods=['GET'])
def all_post():
	query = Post.query.all()
	post_out = []

	for post in query:
		post_data = {"title": post.title, "author": post.author, "content": post.content, "created_date": post.created_date}
		post_out.append(post_data)

	return {"Posts": post_out}
