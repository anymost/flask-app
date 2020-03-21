from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
def main(name):
    return render_template('hello.html', name=name)
