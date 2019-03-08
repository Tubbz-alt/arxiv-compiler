"""Application factory for compiler service."""

import logging

from werkzeug.exceptions import Forbidden, Unauthorized, NotFound, \
    InternalServerError, BadRequest

from flask import Flask, jsonify

from arxiv.base import Base
from arxiv.users import auth
from arxiv.base.middleware import wrap, request_logs

from .services import store, FileManager
from . import routes


def jsonify_exception(error):
    """Render exceptions as JSON."""
    exc_resp = error.get_response()
    response = jsonify(reason=error.description)
    response.status_code = exc_resp.status_code
    return response


def create_app() -> Flask:
    """Create an instance of the compiler service app."""
    app = Flask(__name__)
    FileManager.init_app(app)
    store.init_app(app)
    app.config.from_pyfile('config.py')

    Base(app)
    auth.Auth(app)

    app.register_blueprint(routes.blueprint)
    app.errorhandler(Forbidden)(jsonify_exception)
    app.errorhandler(Unauthorized)(jsonify_exception)
    app.errorhandler(BadRequest)(jsonify_exception)
    app.errorhandler(InternalServerError)(jsonify_exception)
    app.errorhandler(NotFound)(jsonify_exception)

    wrap(app, [auth.middleware.AuthMiddleware])

    return app
