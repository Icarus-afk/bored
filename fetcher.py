import requests

global store

def get_data():
    resp = requests.get('https://www.boredapi.com/api/activity')
    store = resp.json()
    return store['activity']
