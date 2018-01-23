import requests
import json

class Joke():
	"""A class for jokes"""
	def get_random(self):
		resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
		joke_data = json.loads(resp.text)
		return joke_data['joke']


class User()
	"""A class for users"""
	pass
