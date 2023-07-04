# IMDb API

**IMDb API** is a Python script that allows you to parse IMDb movie, series, and episode pages to extract JSON data embedded in script tags.

## Features

- Retrieve a JSON of content from IMDb movie, series, and episode pages.

## Requirements

- Python 3.X
- BeautifulSoup
- Requests

## Usage

1. Install the required dependencies mentioned in the Requirements section.
2. Import the `imdbApi` module into your Python script:

   ```python
   from imdbApi import IMDBApi

   jsonFetched = IMDBApi(imdbCode='tt1615550').search()

## Limitations
- This project relies on the structure and formatting of IMDb pages. Changes to IMDb's HTML structure may require updates to the parser.

## Contributing
- Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please submit a pull request or open an issue in this repository.

## License
This project is licensed under the [GNU General Public License v3.0](LICENSE).
