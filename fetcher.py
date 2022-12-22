import requests

def get_data():
    resp = requests.get('https://www.boredapi.com/api/activity')
    store = resp.json()
    return store['activity']
