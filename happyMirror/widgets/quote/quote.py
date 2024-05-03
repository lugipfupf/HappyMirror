import os
import shutil
import importlib
import random

import requests
import json

from flask import render_template_string

from happyMirror.render import BaseRenderer, RenderResult

from happyMirror.httplib import HttpError, BadRequest


class Renderer(BaseRenderer):

    def __init__(self, alt_config=None) -> None:
        self.config = alt_config
        if self.config is None:
            self.config = self.__check_config()

    def next(self, category=None):
        url = self.config.api_url
        if category is not None:
            url = url + '?category={}'.format(category)

        response = requests.get(
            url, headers={'X-Api-Key': self.config.api_key}, timeout=10
        )

        if response.status_code == 200:
            return json.loads(response.text)
        if response.status_code == 400:
            raise BadRequest(json.loads(response.text))

        raise HttpError(json.loads(response.text))

    def render(self) -> RenderResult:
        category = None

        if self.config.categories is not None:
            category = random.choice(self.config.categories)

            {'error': 'Invalid API Key.'}

        try:
            quote = self.next(category)
            return {
                'view': render_template_string('{{ quote[0]["quote"] }} - {{ quote[0]["author"] }}', quote=quote),
                'name': 'quote'
            }
        except HttpError as e:
            return {
                'view': render_template_string('Quote Widget: {{ error["error"] }}', error=e.args[0]),
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
