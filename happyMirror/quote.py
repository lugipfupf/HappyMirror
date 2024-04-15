import random
import requests
import json

from . import quote_categories



class Quote():
    def __init__(self) -> None:
        self.url = 'https://api.api-ninjas.com/v1/quotes?category='


    def next(self):
        category = random.choice(quote_categories.categories)

        quote = requests.get(
            self.url + category, headers={'X-Api-Key': 'your-api-key'}, timeout=10
        )

        return json.loads(quote.text)
