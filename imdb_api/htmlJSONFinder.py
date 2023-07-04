import json
from bs4 import BeautifulSoup


def findJSONInHTML(html: str):
    parser = BeautifulSoup(html, 'html.parser')
    scriptTags = parser.findAll('script')

    for script in scriptTags:
        if 'pageProps' in script.text:
            return json.loads(s=script.text)

    return {}
