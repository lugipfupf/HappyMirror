from happyMirror.render import BaseRenderer


class Widget:
    def __init__(self, module, instance: BaseRenderer):
        self.module = module
        self.instance = instance