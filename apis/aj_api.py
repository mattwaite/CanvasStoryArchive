"""
Talks to the Al Jazeera Story API.
Requres a valid AJ_API_KEY environment variable.
"""
import os
import requests

AJ_API_LANGUAGE = 'en'
BASE_URL = 'http://devapi.aljazeera.com/v1/'+AJ_API_LANGUAGE+'/stories/'
AJ_API_KEY = os.getenv('ALJAZEERA_API_KEY')
#AJ_API_SECRET = os.getenv('ALJAZEERA_API_SECRET')

def story(section, pagesize=15, pagenumber=1):
    params = {
        'format': 'json',
        'apikey': AJ_API_KEY,
        'pagesize': pagesize,
        'pagenumber': pagenumber
    }
    endpoint = BASE_URL + section
    r = requests.get(endpoint, params=params)
    return r.json()