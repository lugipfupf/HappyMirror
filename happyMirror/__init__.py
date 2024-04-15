import os
import importlib
import sys

from flask import Flask, render_template
import config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # quote  = Quote()

    @app.route('/')
    def root():
        return 'blah'
        # return render_template('base.html', quote=quote.next())

    return app


def load_widgets(enabled_widgets=None):
    if enabled_widgets is None:
        enabled_widgets = []

    for root, dirs, files in walklevel(os.curdir + '/widgets'):
        for dir_name in dirs:
            if dir_name in enabled_widgets:
                sys.path.append(root)
                print(f"Importing widget '{dir_name}'")
                widget_package = importlib.import_module(dir_name)
                print(f"Widget '{widget_package.__name__}' loaded")


def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


if __name__ == '__main__':
    load_widgets(config.enabled_widgets)
    # create_app().run()
