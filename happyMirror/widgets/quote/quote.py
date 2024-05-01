import os
import shutil
import importlib
import random
import sys

import requests
import json

from flask import render_template_string

from happyMirror.render import BaseRenderer, RenderResult


class Renderer(BaseRenderer):

    def __init__(self, alt_config=None) -> None:
        self.config = alt_config
        if self.config is None:
            self.config = self.__check_config()

    def next(self, category=None):
        if len(self.config.api_key) != 40:
            return [{
                "quote": "NO API KEY SET IN CONFIG FILE",
                "author": "'Quote' widget",
                "category": category,
            }]

        url = self.config.api_url
        if category is not None:
            url = url + '?category={}'.format(category)

        quote = requests.get(
            url, headers={'X-Api-Key': self.config.api_key}, timeout=10
        )

        return json.loads(quote.text)

    def render(self) -> RenderResult:
        category = None

        if self.config.categories is not None:
            category = random.choice(self.config.categories)

        quote = self.next(category)
        return {
            'view': render_template_string('{{ quote[0]["quote"] }} - {{ quote[0]["author"] }}', quote=quote),
            'name': 'quote'
        }

    @staticmethod
    def __check_config():
        config_file = f"{os.getcwd()}/widgets/quote/quote_config.py"
        config_example_file = f"{os.getcwd()}/widgets/quote/quote_config_example.py"

        if os.path.isfile(config_file) is False:
            print(f'No config file was found. A new one will be created as "{config_file}"')
            print('Open it and insert your api key, then restart the application.')

            shutil.copy(config_example_file, config_file)

        return importlib.import_module('quote_config')



