def createURL(imdbCode: str) -> str:
    return f'https://imdb.com/title/{imdbCode.lower().strip().rstrip()}'
