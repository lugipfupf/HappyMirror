from abc import ABC, abstractmethod
from typing import TypedDict

from flask import Flask


class RenderResult(TypedDict, total=False):
    script: str
    view: str
    name: str


class BaseRenderer(ABC):
    def register_custom_routes(self, app: Flask):
        pass

    @abstractmethod
    def render(self) -> RenderResult:
        pass

