import json
import requests
from product import Product

def getAllProducts():
    productList = []
    res = requests.get('http://localhost:5000/api/database')
    res = res.json()
    productsRes = res["productList"]
    for productRes in productsRes:
        productName = productRes["product"]["name"]
        productPrice = float(productRes["product"]["price"])
        product = Product(productName, productPrice)
        productList.append(product)
    return productList