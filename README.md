# Colorado lottery data
Some Python to download and parse [a bunch of Colorado lotto spreadsheets](https://www.coloradolottery.com/en/player-tools/whos-winning/) into a flat CSV.

## Setup
Needs Python >=3.5 (love those f-strings!), and I'm using [`pipenv`](http://pipenv.readthedocs.io/) to manage the dependencies (`pandas`, `xlrd`, `requests` and `bs4`).

## Run the code
1. Clone or download this repository and `cd` into the directory
2. (If using pipenv) `pipenv install` (otherwise, use the management tooling of your choice to create a virtual environment and install the dependencies)
3. `pipenv shell`
4. `python download.py`
5. `python process.py`