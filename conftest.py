import pytest
from module.api.clients.github import GitHub
from module.common.database import Database


class User:

    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = ""
        self.second_name = ""

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    github = GitHub()
    yield github


@pytest.fixture
def database():
    db = Database()

    yield db

    db.connection.close()

