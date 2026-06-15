import requests

api = "https://jsonplaceholder.typicode.com/posts/1"  # free public REST API, no auth required

response = requests.get(api)   # sends GET request, reads & decodes automatically
print(response.text)           # .text gives you the already-decoded string