import pytest
from urlCreator import createURL


@pytest.fixture()
def expectedURL():
    return 'https://imdb.com/title/tt1798709'


def test_shouldCreateURLBasedOnIMDBCode(expectedURL):
    assert createURL('tt1798709') == expectedURL


def test_shouldCreateURLBasedOnIMDBCodeConvertingToLowerCase(expectedURL):
    for code in ['TT1798709', 'Tt1798709', 'tT1798709']:
        assert createURL(code) == expectedURL


def test_shouldCreateURLBasedOnIMDBCodeEvenIfCodeStartsOrEndsWithSpace(expectedURL):
    for code in [' TT1798709', 'Tt1798709 ', '   tT1798709    ']:
        assert createURL(code) == expectedURL
