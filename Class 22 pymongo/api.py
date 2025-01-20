import requests # type: ignore
data=requests.get('https://dummyjson.com/products')

print(data.json())
