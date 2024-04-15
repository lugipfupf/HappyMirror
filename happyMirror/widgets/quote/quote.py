import random
import requests
import json

from .quote_categories import categories
from .widget_secrets import api_key


class Quote:
    def __init__(self, secrets_config=None) -> None:
        if secrets_config is None:
            raise "No secrets provided"

        self.url = 'https://api.api-ninjas.com/v1/quotes?category='
        print("Hello Quote")


    def next(self):
        category = random.choice(categories)

        quote = requests.get(
            self.url + category, headers={'X-Api-Key': api_key}, timeout=10
        )

        return json.loads(quote.text)
