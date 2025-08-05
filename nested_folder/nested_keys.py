import os
from config import get_secret

GOOGLE_API_KEY = "AIzaSyDUMMY-KEY-1234567890_abcdefghijklmno_NESTED"
GITHUB_TOKEN = "ghp_DummyToken1234567890AbCdEfGhIjKlMnOpQrStUv_NESTED"

access_key_id = "AKIAVD2S6UYGOO2DCDI3"
secret_key = "1g6CIIxNna2HpuTqAEcHG6xAZ+OdJx0ZE5GQJDU2"

def nested_function():
    try:
        aws_api_key = get_secret("AWS_API_KEY")
        print(f"Nested AWS Key: {aws_api_key}")
        print(f"Nested Google Key: {GOOGLE_API_KEY}")
        print(f"Nested GitHub Token: {GITHUB_TOKEN}")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

nested_function()