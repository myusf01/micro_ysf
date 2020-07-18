from app import app
from flask import render_template


@app.route('/')
@app.route('/index')

def index():
    user = {"username":"Velid"}
    posts = [
        {
            'author':{'username': 'Velid'},
            'body':'You beautyy!'
        },
        {
            'author':{'username': 'Els'},
            'body':'Yeaap!'
        }
    ]

    return render_template("index.html", title='Home', user=user,posts=posts)
