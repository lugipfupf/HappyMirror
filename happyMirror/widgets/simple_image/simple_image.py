import os

from flask import Flask, render_template_string, send_from_directory

from happyMirror.render import BaseRenderer, RenderResult


class Renderer(BaseRenderer):
    def register_custom_routes(self, app: Flask):
        print(f"Widget '{__name__}' is registering custom routes...")
        app.add_url_rule(
            '/widgets/simple_image/images/<path:image_file>', view_func=self.send_image
        )

    def send_image(self, image_file):
        image_dir = os.path.dirname(os.path.relpath(__file__)) + '/images'
        return send_from_directory(image_dir, image_file)

    def render(self) -> RenderResult:
        image = '/' + os.path.dirname(os.path.relpath(__file__)) + '/images/640px-Youngkitten.jpg'
        return {
            'view': render_template_string('<img src="{{ image }}" />', image=image)
        }
