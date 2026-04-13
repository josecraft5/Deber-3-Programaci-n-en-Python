import requests

url = "https://example.com/"
req = requests.get(url)

print(req)
print(req.status_code)