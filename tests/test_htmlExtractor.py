import pytest
import htmlExtractor
from unittest.mock import patch


@pytest.fixture()
def url() -> str:
    return 'https://imdb.com/title/tt6723592'


@patch('htmlExtractor.requests.get')
def test_shouldReturnStringContainingHTMLContentWhenRequestStatusCodeIs200(mocked_function, url):
    mocked_function.return_value.status_code = 200
    mocked_function.return_value.text = '<html>Saint Laurent Mask</html>'

    html = htmlExtractor.extract(url)
    
    assert html.startswith('<html>')
    assert mocked_function.called


@patch('htmlExtractor.requests.get', side_effect=Exception)
def test_shouldReturnFalseWhenAnExceptionIsHandled(mocked_function, url):
    assert not htmlExtractor.extract(url)
    assert mocked_function.called
    assert mocked_function.call_count == 1
