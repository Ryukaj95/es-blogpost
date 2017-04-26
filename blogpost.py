from flask import Flask, render_template
import collections
app = Flask(__name__)

@app.route('/')
def apri_Home():
    return render_template('blog.html')
