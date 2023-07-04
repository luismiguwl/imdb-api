from setuptools import setup, find_packages


setup(
    name='imdb-api',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'bs4'
    ],
    author='Luis Miguel',
    author_email='luisbwrb@gmail.com',
    description='A easier way to scrap IMDB movies and shows',
    license='GNU General Public License v3.0',
    keywords='python, imdb, movie-api, imdb-webscrapping, imdb-api, imdb-python, imdb-scraper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/luismiguwl/imdb-api'
)
