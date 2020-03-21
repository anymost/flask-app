from flask import Flask

app = Flask(__name__)


@app.route('/user/<string:user_id>')
def hello_world(user_id: int):
    """
        int,float,string,path
    """
    print(user_id)
    return 'Hello, %s!' % user_id
