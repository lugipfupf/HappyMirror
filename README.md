# Developing widgets
There a few sample widgets already included. On each page reload, each widgets `render()` method is called and
a dictionary of type`RenderResult` is expected. Structure your module like so:
The widget loader will try to load a class `Renderer` from a file that has the same name as the package.

```python
# filename must be same as package name
from happyMirror.render import BaseRenderer, RenderResult

class Renderer(BaseRenderer):
    def render(self) -> RenderResult:
        # do your stuff
        
        # all fields are optional
        return {
            'name': 'some name', # mainly used for debuggging
            'view': 'html stuff',
            'script': 'javascript'
        }
```

# How to run
## Development mode
Get all you need by typing `pip install -e .`, then run the application directly from VSCode.

## Production mode
Make sure, waitress is installed. On Linux, you can do so by typing `sudo apt install python3-waitress`
Then run `waitress-serve --call 'HappyMirror:create_app'`
