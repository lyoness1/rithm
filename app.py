# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

# local cache of all jokes. Will reset with server reboot. 
all_jokes = {}

def _get_random_joke():
    # get a random joke from the external API
    resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke_data = json.loads(resp.text)
    joke_id = str(joke_data['id'])

    # store joke in local cache
    if joke_id not in all_jokes:
        # Not all jokes are able to be cast to strings
        try:
            # create joke dictionary with up and down vote counts
            joke = {
                'id': joke_id,
                'joke': str(joke_data['joke']),
            }
            joke['up_votes'] = 0
            joke['down_votes'] = 0
            all_jokes[joke_id] = joke
        except Exception as e:
            print ("Error: ", e)
    
    return all_jokes[joke_id] if joke_id in all_jokes else None

def _get_jokes():
    # create dictionary of 20 random jokes, checking local cache first to preserve votes
    current_jokes = {}
    while len(current_jokes) <= 20:
        rand_joke = _get_random_joke()
        # return None if joke was not able to be case to string and continue
        joke_id = rand_joke['id'] if rand_joke else None
        # no repeats in current jokes list
        if joke_id and joke_id not in current_jokes:
            # all jokes retrieved through _get_random_joke will be in local cache with votes
            current_jokes[joke_id] = all_jokes[joke_id]

    return current_jokes

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jokes', methods=['GET'])
def jokes():
    """Loads a page with twenty random jokes"""
    jokes = _get_jokes()
    return render_template('home.html', jokes=jokes)

@app.route('/jokes/<string:joke_id>/up-vote', methods=['POST'])
def up_vote(joke_id):
    """Add upvote to a joke"""
    joke = all_jokes[joke_id]
    joke['up_votes'] += 1
    return jsonify(joke)


if __name__ == '__main__':
    app.run(debug=True)
