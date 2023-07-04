import pytest
from re import Match
from typing import List
from imdbCodeValidator import *
from unittest.mock import patch
from models.imdbCode import IMDBCode


@pytest.fixture()
def codes() -> List[dict]:
    return [{'imdbCode': 'tt1345836'}, {'imdbCode': 'tt1798709'}]


@patch('imdbCodeValidator.validateUsingRegex', return_value=False)
def test_shouldReturnNonEmptyListWhenOneOrMoreCodesAreInvalid(mocked_function, codes):
    result = validate(codes)

    assert len(result) == len(codes)

    for item in result:
        assert item.__repr__() == IMDBCode(code=item.code, isValid=item.isValid).__repr__()

    mocked_function.called
    mocked_function.call_count == len(codes)


def test_shouldReturnEmptyListWhenReceivesEmptyListOfCodes():
    assert validate([]) == []


@patch('imdbCodeValidator.re.match', return_value=Match)
def test_shouldReturnTrueIfRegexMatch(mocked_function, codes):
    for code in codes:
        assert validateUsingRegex(code.get('imdbCode'))

    assert mocked_function.called
    assert mocked_function.call_count == len(codes)


@patch('imdbCodeValidator.re.search', return_value=None)
def test_shouldReturnTrueIfRegexMatch(mocked_function, codes):
    for code in codes:
        assert not validateUsingRegex(code.get('imdbCode'))

    assert mocked_function.called
    assert mocked_function.call_count == len(codes)
