import requests

BASE_URL = "https://api.github.com"

def get_user(username):
    url = f"{BASE_URL}/users/{username}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user: {e}")
        return None

def get_repos(username):
    url = f"{BASE_URL}/users/{username}/repos?per_page=100"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repos: {e}")
        return []