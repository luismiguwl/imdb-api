import requests


def extract(url: str) -> str:
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-amazon-internal-ip-location': 'Country=US;'
        }, timeout=60 * 2)

        return response.text
    except Exception as e:
        print(f'Unable to connect with {url}')
        print(e)
        return False
