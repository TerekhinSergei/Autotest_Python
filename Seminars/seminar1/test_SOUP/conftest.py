import pytest


@pytest.fixture()
def valid_word():
    return 'молоко'


@pytest.fixture()
def invalid_word():
    return 'малоко'