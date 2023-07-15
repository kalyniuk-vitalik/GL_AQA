import pytest


@pytest.mark.check
def test_check_name(user):
    assert user.name == "Vitalik"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Kalyniuk"
