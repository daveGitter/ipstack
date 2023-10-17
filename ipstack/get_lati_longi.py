#!/usr/bin/env python3

""" A CLI app to query the IPStack API. """

import json
import sys
from typing import Optional
from urllib.error import URLError, HTTPError 
import urllib.request


API_URL = 'http://api.ipstack.com/'
API_KEY = '72f68adf76316ca7faaa5a5c04b433b6'


def main() -> Optional[tuple[float, float]]:
    """ Return latitude and logitude of a give ip-address.
    Return None if anythong wrong during getting response from the website.
    """
    ip_addr = sys.argv[1]
    url = f'{API_URL}{ip_addr}?access_key={API_KEY}'

    try:
        rsp = urllib.request.urlopen(url)
    except HTTPError as eh:
        print(f'Oops! Something wrong: {eh.msg}. Please try again. Bye!')

        return None
    except URLError as eu:
        print(f'Oops! Connection error: {eu.reason}. Please try again. Bye!')

        return None

    text = json.loads(rsp.read().decode())
    lati = text["latitude"]
    logi = text["longitude"]

    print(f'Geoinfo for {ip_addr}')
    print(f'Latitude: {lati}, Longitude: {logi}')

    return (lati, logi)


if __name__ == '__main__':
    main()
