import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

user_message = "hi how are you doing today?"

request_message = {"message": user_message}

url = os.getenv("N8N_WEBHOOK_TEST_URL")

response = requests.post(url, json=request_message)

print(response.status_code)

# print(response.json()[0]["output"])
