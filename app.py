from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jokes', methods=['GET'])
def get_jokes():
    resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke_data = json.loads(resp.text)
    joke_text = joke_data['joke']


if __name__ == '__main__':
    app.run(debug=True)
