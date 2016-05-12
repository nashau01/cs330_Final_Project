import requests

res = requests.get("http://www.hotslogs.com")

print(res.text)