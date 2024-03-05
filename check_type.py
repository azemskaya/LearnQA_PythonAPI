import requests

method_dict = ['GET', 'POST', 'PUT', 'DELETE']
base_url = "https://playground.learnqa.ru/api/compare_query_type"
# 1 простой запрос без method
response_simple = requests.request(method_dict[0], base_url)
print(f"Запрос без method: {response_simple.text}")
# 2 запрос head
response_head = requests.head(base_url)
print(f"Запрос head: {response_head}")
# 3 запрос с method
response_method = requests.request(method_dict[0], base_url, params={"method": f"{method_dict[0]}"})
print(f"Запрос c method: {response_method.text}")
# 4 проверки в цикле
for method in range(4):
    response_get = requests.request(method_dict[0], base_url, params={"method":f"{method_dict[method]}"})
    print(f"Запрос get, значение method: {method_dict[method]}, ответ: {response_get.text}")

for req in [1,2,3]:
  for method in range(4):
    response_request = requests.request(method_dict[req], base_url, data={"method":f"{method_dict[method]}"})
    print(f"Запрос {method_dict[req]}, значение method: {method_dict[method]}, ответ: {response_request.text}")

