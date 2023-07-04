from htmlJSONFinder import findJSONInHTML


def test_shouldReturnJSONIfTheresPagePropsInHTMLScriptTagContent():
    html = """
    <html>
        <script>{"pageProps": {"name": "Tenet", "releasedYear": 2020, "tconst": "tt6723592"}}</script>
    </html>
    """

    assert findJSONInHTML(html) == {"pageProps": {"name": "Tenet", "releasedYear": 2020, "tconst": "tt6723592"}}


def test_shouldReturnEmptyJSONIfTheresNoPagePropsInHTMLScriptTagContent():
    html = """
    <html>
        <script>{"name": "Tenet", "releasedYear": 2020, "tconst": "tt6723592"}</script>
    </html>
    """
    
    assert findJSONInHTML(html) == {}


def test_shouldReturnEmptyDictWhenTheresNoScriptTagOnHTML():
    html = """
    <html>
        <h1>No script tag here!</h1>
    </html>
    """

    assert findJSONInHTML(html) == {}


def test_shouldReturnEmptyDictWhenScriptTagExistsButIsEmpty():
    html = """
    <html>
        <script></script>
    </html>
    """

    assert findJSONInHTML(html) == {}
