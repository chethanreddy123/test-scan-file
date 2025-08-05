import os

def get_secret(key):
    secret = os.getenv(key)
    if secret is None:
        raise ValueError(f"Environment variable '{key}' not found.")
    return secret