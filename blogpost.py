from flask import Flask, render_template
import collections

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('blog.html')
