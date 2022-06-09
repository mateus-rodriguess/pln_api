import requests


data = {
    "message": "I am really happy",
    "user": "mateus"
}

url = "http://localhost:8090/accuracy"

response = requests.post(url=url, json=data)

print(response.content)
