import requests
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
API_KEY="19e9712d60f01cc61eb6571c9ba428fb"
CITY="London"

request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"
response=requests.get(request_url)

if response.status_code == 200:
    print("Success the request was fulfilled.")
else:
    print(f"Error: the request is faild with status code {resonse.status_code}")




    