import base64
import os

from flask import render_template_string

from happyMirror.render import BaseRenderer, RenderResult


class Renderer(BaseRenderer):
    def render(self) -> RenderResult:
        image = '/' + os.path.dirname(os.path.relpath(__file__)) + '/images/01.png'
        print(image)

        return {
            'view': render_template_string('<img src="{{ image }}" />',  image=image)
        }


