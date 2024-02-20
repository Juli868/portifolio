#!/usr/bin/python3
"""Get data from an api."""
import requests
from os import getenv

api_key = getenv('API_key_kiwi')
url = 'https://tequila-api.kiwi.com/v2/search'

params = {
    'fly_from': 'KGL',  # Example: Prague
    'date_from': '01/08/2024',
    'date_to': '15/08/2024',
}
headers = {'apikey': api_key}


def get_data():
    """Use get method get all data from kiwi site."""
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return (data)
    else:
        return (
                'Failed to retrieve data:',
                response.status_code,
                response.text)
