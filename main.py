from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["post"])
def main():
    print(request.headers)
    print(request.form['user'])
    return 'hello'
