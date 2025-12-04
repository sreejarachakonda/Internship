import requests

BASE_URL = "http://localhost:3000/characters"

def get_characters():
    return requests.get(BASE_URL).json()

def get_character(id):
    return requests.get(f"{BASE_URL}/{id}").json()

def create_character(data):
    return requests.post(BASE_URL, json=data).json()

def update_character(id, data):
    return requests.put(f"{BASE_URL}/{id}", json=data).json()

def delete_character(id):
    return requests.delete(f"{BASE_URL}/{id}").json()
