import requests
import time

token = input("Please enter your token: ")
channel_id = input("Please enter the channel ID: ")

api_url = f'https://discord.com/api/v9/channels/{channel_id}/typing'
headers = {'Authorization': token}

first_time = True

while True:
    response = requests.post(api_url, headers=headers)
    if response.status_code == 204:
        if first_time:
            print("Always typing enabled.")
            first_time = False
    else:
        print(f"Received wrong status code: {response.status_code}")
    time.sleep(8)

