import vonage
import requests

# Function to send an SMS
def send_sms(api_key, api_secret, from_value, to_value, text_value):
    client = vonage.Client(key=api_key, secret=api_secret)
    sms = vonage.Sms(client)

    # Send the SMS message
    responseData = sms.send_message(
        {
            "from": from_value,
            "to": to_value,
            "text": text_value,
        }
    )

    # Check if the message was sent successfully
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

# Ask the user if they want to use their own API credentials
use_own_credentials = input("Do you want to use your own Vonage API credentials? Our may not work (y/n): ").strip().lower()

if use_own_credentials == 'y':
    # Get user input for their API key and secret
    print("Go to nexmo.com to get API credentials?")
    print("This may require you to pay.")
    api_key = input("Enter your Vonage API key: ")
    api_secret = input("Enter your Vonage API secret: ")
else:
    # URLs where API credentials are stored
    api_key_url = "https://cyber.dbot.cc/key"
    api_secret_url = "https://cyber.dbot.cc/private"

    # Fetch API credentials from the web
    api_key_response = requests.get(api_key_url)
    api_secret_response = requests.get(api_secret_url)

    if api_key_response.status_code == 200 and api_secret_response.status_code == 200:
        api_key = api_key_response.text.strip()
        api_secret = api_secret_response.text.strip()
    else:
        print("Failed to fetch API credentials from the web. Please check the URLs.")
        exit(1)  # Exit the script if fetching credentials fails

# Get user input for the message details
from_value = input("Enter the sender information: ")
to_value = input("Enter the 'to' value (recipient's phone number): ")
text_value = input("Enter the SMS text message: ")
send_count = int(input("Enter how many times you want to send the message: "))

# Send the SMS message the specified number of times
for _ in range(send_count):
    send_sms(api_key, api_secret, from_value, to_value, text_value)
