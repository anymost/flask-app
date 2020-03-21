from flask import Flask, request

app = Flask(__name__, static_folder='static')


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return 'get home'
    else:
        return 'post home'
