import requests
from requests.auth import HTTPBasicAuth

USERNAME = ''
TOKEN = ''

users_to_follow = [
    
]

def follow_user(username):
    url = f'https://api.github.com/user/following/{username}'
    response = requests.put(url, auth=HTTPBasicAuth(USERNAME, TOKEN))
    
    if response.status_code == 204:
        print(f'Followed: {username}')
    else:
        print(f'Failed to follow {username}. Status code: {response.status_code}, Response: {response.json()}')

for user in users_to_follow:
    follow_user(user)