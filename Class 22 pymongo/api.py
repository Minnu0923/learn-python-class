import requests
data=requests.get('https://dummyjson.com/products')

print(data.json())