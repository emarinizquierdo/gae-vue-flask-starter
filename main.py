import logging
import os

from flask import Flask, Blueprint, json

import src
import vue

from src.api.endpoints.item import ns as items_namespace
from src.restplus import api

def set_log_level():
    logging.getLogger().setLevel(logging.INFO)

set_log_level()

app = Flask(__name__)

def create_app(flask_app):

    #flask_app.config.from_object(config.get_config())
    #flask_app.config.from_pyfile('../config.py', silent=True)

    blueprint = Blueprint('s', __name__, url_prefix='/s')
    #blueprint.before_request(BeforeRequestFlow(oauth_filter=False))
    api.init_app(blueprint)
    api.add_namespace(items_namespace)

    #flask_app.register_blueprint(swgrjson.swaggerjson)
    #flask_app.register_blueprint(swagger.swagger_bp)
    flask_app.register_blueprint(blueprint) 
    flask_app.register_blueprint(vue.vue, url_prefix='')

create_app(app)