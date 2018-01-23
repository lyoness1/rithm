from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

all_jokes = {}

def _get_random_joke():
    resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke_data = json.loads(resp.text)
    if joke_data['id'] not in all_jokes:
        all_jokes[joke_data['id']] = joke_data
    return joke_data

def _get_jokes():
    current_jokes = {}
    for i in range(20):
        rand_joke = _get_random_joke()
        if rand_joke['id'] not in current_jokes:
            current_jokes[rand_joke['id']] = rand_joke['joke']
    return current_jokes

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jokes', methods=['GET'])
def jokes():
    jokes = _get_jokes()
    print ("Jokes", jokes)
    return render_template('home.html', jokes=jokes)


if __name__ == '__main__':
    app.run(debug=True)
