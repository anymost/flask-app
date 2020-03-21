from flask import Flask, url_for

app = Flask(__name__)


@app.route("/user/")
def user():
    """ 如果是/user 会自动重定向到/user/"""
    return 'hello user'


@app.route("/about")
def about():
    """ 如果是/about 会404"""
    val = url_for('about', name="jack")
    print(val)
    return 'hello about'


