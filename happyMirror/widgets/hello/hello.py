from happyMirror.render import RenderResult, BaseRenderer


class Renderer(BaseRenderer):
    def __init__(self, config=None, secrets_config=None) -> None:
        pass

    def render(self) -> RenderResult:
        return { 'view': '<h1>Hello World!</h1>', 'name': 'hello' }
