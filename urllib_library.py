from urllib.request import urlopen
api = "https://jsonplaceholder.typicode.com/posts/1"

with urlopen(api) as response:
    data = response.read()
    string = data.decode()
    print(string)