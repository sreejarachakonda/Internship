import requests

BASE_URL = "http://localhost:3000/battles"

def get_battles():
    return requests.get(BASE_URL).json()

def get_battle(id):
    return requests.get(f"{BASE_URL}/{id}").json()

def create_battle(data):
    return requests.post(BASE_URL, json=data).json()

def update_battle(id, data):
    return requests.put(f"{BASE_URL}/{id}", json=data).json()

def delete_battle(id):
    return requests.delete(f"{BASE_URL}/{id}").json()
