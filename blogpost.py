from flask import Flask, render_template
import collections
import peewee as p

app = Flask(__name__)
db = p.SqliteDatabase('posts.db')


class Post(p.Model):

    id = p.IntegerField()
    title = p.CharField()
    content = p.CharField()
    data = p.CharField()

    class Meta:
        database = db
        db_table = "posts"


@app.route('/')
def home():
    return render_template('blog.html', post=Post.select())


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')
