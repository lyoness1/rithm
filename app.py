# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

all_jokes = {}

def _get_random_joke():
    # get a random joke from the external API
    resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke_data = json.loads(resp.text)
    joke_id = joke_data['id']

    # store joke in local cache
    if joke_id not in all_jokes:
        joke_data['up_votes'] = 0
        joke_data['down_votes'] = 0
        all_jokes[joke_id] = joke_data
    
    return all_jokes[joke_id]

def _get_jokes():
    # create dictionary of 20 random jokes, checking local cache first to preserve votes
    current_jokes = {}
    while len(current_jokes) <= 20:
        rand_joke = _get_random_joke()
        joke_id = rand_joke['id']
        # no repeats in current jokes list
        if joke_id not in current_jokes:
            # all jokes retrieved through _get_random_joke will be in local cache with votes
            current_jokes[joke_id] = all_jokes[joke_id]

    return current_jokes

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jokes', methods=['GET'])
def jokes():
    jokes = _get_jokes()
    return render_template('home.html', jokes=jokes)


if __name__ == '__main__':
    app.run(debug=True)
