from flask import Flask, render_template, request, redirect, url_for
import collections
import peewee as p
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
db = p.SqliteDatabase('posts.db')


def insert_post_into_database(form_title, form_date, form_content):
    query = Post.insert(title=form_title, data=form_date, content=form_content)
    query.execute()


class Post(p.Model):

    id = p.IntegerField()
    title = p.CharField()
    content = p.CharField()
    data = p.CharField()

    class Meta:
        database = db
        db_table = "posts"


@app.route('/home')
def home():
    return render_template('blog.html', post=Post.select())


@app.route('/submit', methods=["POST"])
def submit():
    print("ciao")
    insert_post_into_database(
        request.form['title'], request.form['date'], request.form['content'])
    return redirect(url_for("home"))


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')


class NewPost(Resource):
    def post(self):
        data = request.get_json()
        insert_post_into_database(data[
            'title'], data['date'], data['content'])


api.add_resource(NewPost, '/home')
