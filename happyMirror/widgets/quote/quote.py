import random
import requests
import json

from flask import render_template_string

from happyMirror.render import BaseRenderer, RenderResult

try:
    import widget_secrets
    import widget_config
except ImportError:
    from . import widget_secrets
    from . import widget_config


class Renderer(BaseRenderer):

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

    def render(self) -> RenderResult:
        quote = self.next()
        return {
            'view': render_template_string('{{ quote[0]["quote"] }} - {{ quote[0]["author"] }}', quote=quote),
            'name': 'quote'
        }
