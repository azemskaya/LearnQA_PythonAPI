import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response.json()['token']
sleep_time = response.json()['seconds']
print(response.json())
response_status = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
resp = response_status.json()
if not "status" in resp:
    print(f"Unexpected response {resp}")
elif not resp['status'] == 'Job is NOT ready':
    print(f"Unexpected status {resp['status']}")
else:
    print(resp)


time.sleep(sleep_time)
response_ready = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
resp = response_ready.json()
if not "status" in resp:
    print(f"Unexpected response {resp}")
elif (not resp['status'] == 'Job is ready') and ('result' in resp):
    print(f"Unexpected response {resp}")
else:
    print(resp)