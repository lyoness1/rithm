from flask import Flask, render_template, jsonify
import requests

from model import Joke

app = Flask(__name__)


def _get_jokes():
    joke = Joke()
    jokes = set()
    for i in range(20):
        rand_joke = joke.get_random()
        if rand_joke not in jokes:
            jokes.add(rand_joke)
    return jokes

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jokes', methods=['GET'])
def jokes():
    jokes = _get_jokes()
    return render_template('home.html', jokes=jokes)

# @app.route('/ajax/jokes', methods=['GET'])
# def get_jokes():
#     jokes = _get_jokes()
#     return jsonify(jokes)


if __name__ == '__main__':
    app.run(debug=True)
