AWS_API_KEY = "AKIAIOSFODNN7EXAMPLE_NESTED"
GOOGLE_API_KEY = "AIzaSyDUMMY-KEY-1234567890_abcdefghijklmno_NESTED"
GITHUB_TOKEN = "ghp_DummyToken1234567890AbCdEfGhIjKlMnOpQrStUv_NESTED"

def nested_function():
    print(f"Nested AWS Key: {AWS_API_KEY}")
    print(f"Nested Google Key: {GOOGLE_API_KEY}")
    print(f"Nested GitHub Token: {GITHUB_TOKEN}")

nested_function()