import requests

responce = requests.get('https://roadmap.sh/python')

print(responce.status_code)
print(responce.ok)

print(responce.text)