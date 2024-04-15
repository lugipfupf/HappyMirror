"""
dasdsa
"""

import os

from flask import Flask, render_template
from happyMirror.quote import Quote


def create_app(test_config=None):
    """
    dsadsa
    """
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

    quote  = Quote()


    @app.route('/')
    def root():
        return render_template('base.html', quote=quote.next())


    return app


if __name__ == '__main__':
    create_app().run()
