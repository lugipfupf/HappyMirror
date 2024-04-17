import os

from happyMirror.render import RenderResult, BaseRenderer


class Renderer(BaseRenderer):
    def __init__(self, config=None, secrets_config=None) -> None:
        pass

    def render(self) -> RenderResult:
        # script_path = os.path.realpath(__file__).resolve('/static/js/clock.js')
        script_path = os.path.dirname(os.path.relpath(__file__)) + '/static/js/clock.js'
        print("script_path: ", script_path)

        return {
            'script': open(script_path, 'r').read(),
            'view': '<h3 id="fulldate" class="u-pull-right"></h3>',
            'name': 'clock'
        }
