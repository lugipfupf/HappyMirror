import os
import importlib
import sys

from flask import Flask, render_template

try:
    import config
except ImportError:
    from . import config


def create_app(widgets=None, test_config=None):
    if widgets is None:
        widgets = []

    widgets = list(filter(lambda w: w is not None, widgets))

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()

    if test_config is None:
        app.config.from_pyfile('widget_config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    for widget in widgets:
        widget['instance'] = widget['module'].Renderer()
        widget['instance'].register_custom_routes(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def root():
        data = []

        for cur_widget in widgets:
            try:
                data.append(cur_widget['instance'].render())
            except KeyError as e:
                print(f"KeyError for: '{cur_widget}'", e)
            except AttributeError:
                print("The module does not have the specified class or function.")
            except Exception as e:
                print(f"Exception for: '{cur_widget}'", e)

        return render_template('base.html', data=data)
    return app


def load_widgets(enabled_widgets=None):
    loaded_widgets = []
    if enabled_widgets is None:
        enabled_widgets = []

    for root, dirs, files in walk_level(os.curdir + '/widgets'):
        for dir_name in dirs:
            single_widget = load_single_widget(dir_name, enabled_widgets, root)
            loaded_widgets.append(single_widget)

    return loaded_widgets


def load_single_widget(dir_name, enabled_widgets, root):
    if dir_name in enabled_widgets:
        try:
            sys.path.append(f"{root}/{dir_name}")
            print(f"Importing widget '{dir_name}'")
            widget_renderer = importlib.import_module(dir_name)
            print(f"Widget '{dir_name}' loaded")

            return {'module': widget_renderer, 'instance': None}
        except ModuleNotFoundError:
            print("Module not found")
        except AttributeError:
            print("The module does not have the specified class or function.")
        except Exception as e:
            print(f"An error occurred while loading widget '{dir_name}': {e}")


def walk_level(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


if __name__ == '__main__':
    my_widgets = load_widgets(config.enabled_widgets)
    create_app(my_widgets).run()
