import requests
import os

def get_content():
    api_url = 'http://api.nytimes.com/svc/news/v3/content/all/all.json'
    payload = {
        'api-key':              '5f5f8663133f4e29935a799b32403139'
    }
    response = requests.get(api_url, params=payload)
    data = response.json() # convert json to python-readable format
    return data

print get_content()