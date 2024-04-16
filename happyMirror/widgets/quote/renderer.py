import os.path
import random
import requests
import json

from flask import Blueprint, Flask, render_template_string

import widget_secrets
import widget_config


class Renderer:
    def __init__(self, config=None, secrets_config=None) -> None:
        if secrets_config is None:
            self.secrets = widget_secrets
        else:
            self.secrets = secrets_config

        if config is None:
            self.config = widget_config
        else:
            self.config = config


    def next(self):
        category = random.choice(self.config.categories)

        quote = requests.get(
            self.config.api_url + category, headers={'X-Api-Key': self.secrets.api_key}, timeout=10
        )

        return json.loads(quote.text)

    def render(self):
        quote = self.next()
        print(f"Quote: {quote[0]}")
        return render_template_string('<h1>{{ quote[0]["quote"] }} - {{ quote[0]["author"] }}</h1>', quote=quote)
