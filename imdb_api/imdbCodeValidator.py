import re
from typing import List
from models.imdbCode import IMDBCode


def validate(codes: List[dict]) -> List[IMDBCode]:
    """
    Validates a list of codes using a regular expression pattern.

    Args:
        codes (List[dict]): A list of dictionaries containing the 'imdbCode' key.
        
    Returns:
        List[IMDBCode]: A list of IMDBCode objects with 'code' and 'isValid' attributes.
        
    Raises:
        None

    Example:
        >>> codes = [{'imdbCode': 'tt12345678'}, {'imdbCode': 'abc12345678'}, {'imdbCode': 'tt1234567'}]
        >>> validate(codes)
        [IMDBCode(code='tt12345678', isValid=True), IMDBCode(code='abc12345678', isValid=False), IMDBCode(code='tt1234567', isValid=True)]
    """
    result = []

    for code in codes:
        onlyCode = code.get('imdbCode')
        result.append(IMDBCode(
            code=onlyCode, isValid=validateUsingRegex(onlyCode)
        ))

    return result


def validateUsingRegex(code: str) -> bool:
    """
    Validates a code string using a regular expression pattern.

    Args:
        code (str): The code string to be validated.

    Returns:
        bool: True if the code string matches the pattern, False otherwise.

    Raises:
        None

    Example:
        >>> validateUsingRegex('tt12345678')
        True
        >>> validateUsingRegex('abc12345678')
        False

    Regular Expression Pattern:
        [t]{2}[0-9]{7,8}$

    - The pattern [t]{2} matches two consecutive 't' characters.
    - [0-9]{7,8} matches 7 to 8 digits.
    - $ asserts the end of the string.
    """
    pattern = re.compile('[t]{2}[0-9]{7,8}$')
    return re.search(pattern=pattern, string=code) is not None
