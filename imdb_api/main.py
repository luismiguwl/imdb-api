import htmlExtractor
import imdbCodeValidator
import htmlJSONFinder
from urlCreator import createURL


def findJSON(imdbCode: str) -> dict:
    if not imdbCodeValidator.validateUsingRegex(imdbCode):
        return {
            'error': 'Invalid code! Provides a code that fit this follow regex: tt{7,8}'
        }

    url = createURL(imdbCode)
    html = htmlExtractor.extract(url)

    if html:
        extractedJSON = htmlJSONFinder.findJSONInHTML(html)
        return extractedJSON

    return None
