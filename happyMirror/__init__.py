import os

from flask import Flask, render_template

# one works when running, one for testing
try:
    import config
except ImportError:
    from . import config

from happyMirror.widgets_loader import WidgetsLoader


def start(widgets_loader: WidgetsLoader, test_config=None):
    widgets = widgets_loader.load(config.enabled_widgets)

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()

    if test_config is None:
        app.config.from_pyfile('widget_config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    for widget in widgets:
        widget.instance.register_custom_routes(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def root():
        data = []

        for cur_widget in widgets:
            try:
                data.append(cur_widget.instance.render())
            except KeyError as e:
                print(f"KeyError for: '{cur_widget}'", e)
            except AttributeError:
                print("The module does not have the specified class or function.")
            except Exception as e:
                print(f"Exception for: '{cur_widget}'", e)

        return render_template('base.html', data=data)

    app.run()

if __name__ == '__main__':
    loader = WidgetsLoader()
    start(widgets_loader=loader)
