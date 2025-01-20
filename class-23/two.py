import requests # type: ignore
import pymongo
data=requests.get('https://dummyjson.com/products')
products=data.json() ['products']
print(type(products))
new_products=[]
for prod in products:
    new_products.append({
        'pid':prod['id'],
        'pname':prod['title'],
        'category':prod['category'],
        'price':prod['price'],
        'rating':prod['rating']
    })

print(len(new_products))
print(new_products)