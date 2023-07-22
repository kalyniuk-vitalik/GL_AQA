import pytest


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
