from flask import Flask, render_template
import collections
import peewee as p

app = Flask(__name__)
db = p.SqliteDatabase('posts.db')

@app.route('/')
def home():
    return render_template('blog.html')
