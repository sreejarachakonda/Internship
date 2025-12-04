import requests

BASE_URL = "http://localhost:3000/kingdoms"

def get_kingdoms():
    return requests.get(BASE_URL).json()

def get_kingdom(id):
    return requests.get(f"{BASE_URL}/{id}").json()

def create_kingdom(data):
    return requests.post(BASE_URL, json=data).json()

def update_kingdom(id, data):
    return requests.put(f"{BASE_URL}/{id}", json=data).json()

def delete_kingdom(id):
    return requests.delete(f"{BASE_URL}/{id}").json()
