import requests
import datetime

def get_users():
    r = requests.get('http://demo/api/users')
    print(r.status_code)
    if r.status_code == 200:
        return r.json()
    return None

def get_today():
    return datetime.datetime.today()
