from flask import Flask
import requests

from model import Joke

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jokes', methods=['GET'])
def get_jokes():
    joke = Joke()
    return joke.get_random()


if __name__ == '__main__':
    app.run(debug=True)
