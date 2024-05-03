![Tests](https://github.com/lugipfupf/HappyMirror/actions/workflows/.github/workflows/python-app.yml/badge.svg)


> *_Note_*
> This project is in a very early development stage. While it will be used by me in a smart mirror project,
> it is also my learning ground for Python.

# How to run
## Virtual Environment
### On Windows:
```shell
venv\bin\activate`
```
### On MacOS / Linux: 
```shell
source venv/bin/activate`
```

### General
```shell
pip install -r requirements.txt
pip install -e .
```

## Testing
While in the root of this repo, simply type `pytest` to run all the tests. Alternatively, if that does not work,
try `pytest-3`.

## Development mode Windows
To run, either start directly from your preferred editor, or, if you have Flask installed, type
```shell
flask --app happyMirror run --debug
```

## Production mode
Make sure, waitress is installed. On Linux, you can do so by typing `sudo apt install python3-waitress`
Then run `waitress-serve --call 'HappyMirror:create_app'`

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

## Custom Routes
If your widget uses custom routes, eg. to display an image, you can do so by implementing `render.BaseRenderer.register_custom_routes`
An example of how to do that can be found in the example widget 'simple_image'.


