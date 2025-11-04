import requests
import os
import hvac

# Initialize Vault client
client = hvac.Client(url=os.environ['VAULT_ADDR'], token=os.environ['VAULT_TOKEN'])

# Define the Vault path for the MongoDB URI
vault_path = 'secret/chethanreddy123/test-scan-file/main.py'

# Fetch the secret from Vault
vault_secret = client.read(vault_path)
mongo_uri_from_vault = vault_secret['data']['data']['secret']

# Dummy AWS API Key (matches pattern like AKIA[0-9A-Z]{16})
AWS_API_KEY = "AKIAIOSFODNN7EXAMPLE"

MONGO = mongo_uri_from_vault	


MONGO_RUN = mongo_uri_from_vault	

# Dummy Google API Key (matches pattern like AIza[0-9A-Za-z\-_]{35})
GOOGLE_API_KEY = "AIzaSyDUMMY-KEY-1234567890_abcdefghijklmno"

# Dummy GitHub Token (matches common GitHub token patterns)
GITHUB_TOKEN = "ghp_DummyToken1234567890AbCdEfGhIjKlMnOpQrStUv"

def fetch_aws_data():
    # Simulating an API call using the hardcoded key
    url = "https://api.example.com/aws-endpoint"
    headers = {"Authorization": f"Bearer {AWS_API_KEY}"}
    response = requests.get(url, headers=headers)
    print("AWS data fetched:", response.status_code)

def fetch_google_data():
    # Simulating a Google API call
    url = f"https://api.google.com/endpoint?key={GOOGLE_API_KEY}"
    response = requests.get(url)
    print("Google data fetched:", response.status_code)

def fetch_github_data():
    # Simulating a GitHub API call
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    print("GitHub data fetched:", response.status_code)

if __name__ == "__main__":
    fetch_aws_data()
    fetch_google_data()
    fetch_github_data()