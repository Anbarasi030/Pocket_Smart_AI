import httpx

response = httpx.get("https://www.example.org/")

print("Status Code:", response.status_code)
print("Request successful!")