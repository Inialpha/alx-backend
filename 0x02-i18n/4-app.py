#!/usr/bin/env python3
""" a simple flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ configure bael """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale() -> str:
    """ return the best match """
    locale = (request.args.get('locale'))
    if locale and locale in ["en", "fr"]:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


# @babel.localeselector
def get_locale() -> str:
    """ return the best match """
    print(request)
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """ an index route """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
