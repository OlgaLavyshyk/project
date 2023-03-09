from json import JSONDecodeError
from bs4 import BeautifulSoup
import requests
from pydantic import BaseModel


class Product(BaseModel):
    brand: str
    id: str
    name: str


class Data:
    products: list[Product]

class Parser:
    def __init__(self):
        self


    def get_product(self, article):
        url = f"https://www.wildberries.ru/catalog/" + str(article) + "/detail.aspx"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"
        }
        try:
            res = requests.get(url,headers)
            json_result = res.text
            s = BeautifulSoup(json_result, parser='html5lib')
            r = s.select('span.hide-mobile')

            for i in r:
                t = i.text
                # print("i",t)

            # print("j = ",r)
        except JSONDecodeError as e:
            print(e)

    def parse_single_article(self, article: str = None):
        return self.get_product(article= article)


    def parse_list_articles(self, articles: list[str] = None):
        data = []
        for art in articles:
            r = self.get_product(article= art)
            data.append(r)

        return data
