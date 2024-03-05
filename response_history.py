import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
response_count = len(response.history)

print(response_count)
print(response.url)