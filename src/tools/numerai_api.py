
import os
import requests
from io import BytesIO
from zipfile import ZipFile


def numerai_api_query(query):
    
    numerai_api_url = 'https://api-tournament.numer.ai/'
    headers = {'Content-Type':'application/json',
               'Accept':'application/json'
              }
    with requests.Session() as r:
        return r.post(url=numerai_api_url,
                      json=query,
                      headers=headers).json()


def get_current_round():
    rounds_query = {'query': '{rounds {number}}'}
    data = numerai_api_query(rounds_query)['data']['rounds']
    round_numbers = [number for rounds in data 
                     for number in rounds.values()]
    round_numbers.sort(reverse=True)
    return round_numbers[0]


def get_dataset_url():
    
    dataset_query = {'query':'{dataset}'}
    return numerai_api_query(dataset_query)['data']['dataset']
