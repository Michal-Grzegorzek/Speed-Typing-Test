import requests


class RandomWord:

    def __init__(self):
        self.endpoint = "https://random-word-api.herokuapp.com/word?number=100"

    def get_random_word(self):
        response = requests.get(self.endpoint)
        response.raise_for_status()
        random_words = response.json()

        return random_words
