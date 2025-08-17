import requests

# Dummy AWS API Key (matches pattern like AKIA[0-9A-Z]{16})
AWS_API_KEY = "AKIAIOSFODNN7EXAMPLE"

MONGO = "mongodb+srv://chethanreddy2002:1234@cluster0.xihwp.mongodb.net/?retryWrites=true&w=majority"	


MONGO_RUN = "mongodb+srv://chethanreddy2002:1234@cluster0.xihwp.mongodb.net/?retryWrites=true&w=majority     "	

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

