#!/usr/bin/env python3
import requests
import subprocess
import time 

limit = 1
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'Your_API_Here'})

new_text = response.text.replace("[{\"fact\": \"", "")
new_text = new_text.replace("\"}]", ".")

print(new_text)

subprocess.call(['notify-send', new_text])

# command =f"notify-send {new_text} {new_text}" 
# subprocess.call(command,  shell=True)
