from abc import ABC, abstractmethod
from typing import TypedDict

class RenderResult(TypedDict, total=False):
    script: str
    view: str
    name: str


class BaseRenderer(ABC):
    @abstractmethod
    def render(self) -> RenderResult:
        pass

