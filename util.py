import requests
from requests.exceptions import HTTPError
import sys


# takes a url and parameters to make a GET request to the integers API and return the response
def get_code_list(URL, PARAMS):
    # getting the response with the 4 random numbers from then API:
    try:
        response = requests.get(
            url=URL, params=PARAMS)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        # Python 3.6
        sys.exit(
            f'HTTP error, unable to generate 4 digit code from random Integer API: {http_err}')
    except Exception as err:
        # Python 3.6
        sys.exit(
            f'Other error occurred, unable to generate 4 digit code from random Integer API: {err}')

    # a list of number strings from the response
    num_str_list = response.text.splitlines()

    return num_str_list


def count_white(x):
    pass


def count_black(x):
    pass
