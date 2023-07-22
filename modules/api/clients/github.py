import pytest
import requests
from requests.exceptions import HTTPError


class GitHub:

    def __init__(self):
        self.url = None
        self.response = None

    def get_user(self, username):
        self.url = f"https://api.github.com/users/{username}"
        self.response = requests.get(self.url)

        try:
            self.response.raise_for_status()
        except HTTPError as http_error:
            print(f"It is a http error: {http_error}")
        return self.response.json()

    def get_repo(self, name):
        self.url = f"https://api.github.com/search/repositories?q={name}"
        self.response = requests.get(self.url)
        self.response.raise_for_status()
        return self.response.json()
