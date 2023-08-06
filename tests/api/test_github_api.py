import pytest
import requests


@pytest.mark.api
def test_user_exists(github_api):
    login_test = github_api.get_user("defunkt")
    assert "login" in login_test


@pytest.mark.api
def test_user_not_exists(github_api):
    login_test = github_api.get_user("johnwick")
    assert login_test["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo_test = github_api.get_repo("become-qa-auto")
    assert repo_test["total_count"] == 42


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo_test = github_api.get_repo("johnwick_repo_non_exist")
    assert repo_test["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo_test = github_api.get_repo("s")
    assert repo_test["total_count"] > 0


@pytest.mark.api
def test_emoji_exists(github_api):
    emoji_page_test = github_api.get_emoji("https://api.github.com/emojis")
    assert "1st_place_medal" in emoji_page_test, "Emoji doesn't exist"
    emoji_url = emoji_page_test["1st_place_medal"]
    emoji_response = requests.head(emoji_url)
    assert emoji_response.status_code == 200


@pytest.mark.api
def test_emoji_not_exist(github_api):
    emoji_page_test = github_api.get_emoji("https://api.github.com/emojis")
    assert "medal_of_honor" not in emoji_page_test, "Emoji exist"


@pytest.mark.api
def test_get_commits_list(github_api):
    commits = github_api.get_commit("octocat", "Hello-World")
    for commit in commits:
        assert "sha" in commit


@pytest.mark.api
def test_get_first_commit(github_api):
    commits = github_api.get_commit("octocat", "Hello-World")
    first_commit = commits[0]
    assert "sha" in first_commit
    assert first_commit["sha"] == "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d"



