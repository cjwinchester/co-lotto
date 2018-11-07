import os
import time

import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://www.coloradolottery.com/en/player-tools/whos-winning/'


def get_categories():
    ''' Grab a list of Colorado lottery game categories '''

    # fetch the page
    r = requests.get(BASE_URL)

    # turn it into soup
    soup = BeautifulSoup(r.text, 'html.parser')

    # target the correct select menu
    select = soup.find('select', {'name': 'game'})

    # return the list of option values
    return [x['value'] for x in select.find_all('option')]

# get those game categories
games = get_categories()

# set up dict of URL parameters
params = {
    'xlsx': '',
    'timeframe': 'sincestart',
    'game': None
}

# loop over the game categories
for game in games:

    # update the params dict
    params['game'] = game

    # fetch xlsx file using those params
    r = requests.get(BASE_URL, params=params)

    # construct a file name
    file_name = f'{game}.xlsx'

    # join it to the raw data directory
    full_path = os.path.join('raw', file_name)

    # open the file
    with open(full_path, 'wb') as f:

        # iterate over response content
        for block in r.iter_content(1024):

            # write to file
            f.write(block)

    # let us know what's up
    print(f'wrote {file_name} ...')

    # pause for 2 seconds
    time.sleep(2)
