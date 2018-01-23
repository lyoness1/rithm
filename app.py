from flask import Flask, render_template
import requests

from model import Joke

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jokes', methods=['GET'])
def get_jokes():
    joke = Joke()
    jokes = []
    for i in range(20):
        jokes.append(joke.get_random())
    return render_template('home.html', jokes=jokes)


if __name__ == '__main__':
    app.run(debug=True)
