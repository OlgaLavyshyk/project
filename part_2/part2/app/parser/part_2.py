import json
import requests
from pydantic import BaseModel


class Product(BaseModel):
    article: str
    brand: str
    title: str


url = "	https://basket-05.wb.ru/vol735/part73512/73512949/info/ru/card.json"
headers = {'Accept': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0"}
response = requests.get(url, headers=headers)
result = response.json()
article = result['nm_id']
brand = result["selling"]['brand_name']
title = result['imt_name']
print(article, brand, title, sep='\n')
product = Product(article=str(article), brand=str(brand), title=str(title))
print(json.loads(product.json()))

