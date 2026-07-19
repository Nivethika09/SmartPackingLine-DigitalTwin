import requests

api_key = "BP5304W2Y6CG9QOE"

url = f"https://api.thingspeak.com/update?api_key={api_key}&field1=10"

response = requests.get(url)

print("Response:", response.text)