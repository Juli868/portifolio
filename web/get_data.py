#!/usr/bin/python3
"""Get data from an api."""
import requests
from os import getenv

params = {
    'fly_from': 'KGL',  # Example: Prague
    'date_from': '01/08/2024',
    'date_to': '15/08/2024',
}


def get_data(
        fly_from=None,
        fly_to=None,
        date_from=None,
        date_to=None,
        currency=None,
        flight_class=None,
        price_min=None,
        price_max=None
        ):
    """Use get method get all data from kiwi site."""
    api_key = getenv('API_key_kiwi')
    params = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            'date_from': date_from,
            'date_to': date_to,
            'curr': currency,
            'selected_cabins': flight_class,
            'prices_to': price_max,
            'prices_from': prices_min
            }
    headers = {'apikey': api_key}
    url = 'https://tequila-api.kiwi.com/v2/search'
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return (data)
    else:
        return (
                'Failed to retrieve data:',
                response.status_code,
                response.text)
