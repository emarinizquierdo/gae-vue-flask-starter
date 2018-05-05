# -*- coding: utf-8 -*-
import os
import flask


vue = flask.Blueprint('vue', __name__, static_url_path='', static_folder='app/dist', template_folder='app/dist')
#front_bp.before_request(BeforeRequestFlow(oauth_filter=False))

@vue.route('/')
def root():
    return vue.send_static_file('index.html')