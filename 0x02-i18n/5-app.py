#!/usr/bin/env python3
""" a simple flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ configure bael """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ return the best match """
    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[Dict, None]:
    """ get_user function """
    user = request.args.get('login_as')
    if user:
        user = users.get(int(user))
    return user


@app.before_request
def before_request() -> None:
    """ before_request function """
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    """ an index route """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
