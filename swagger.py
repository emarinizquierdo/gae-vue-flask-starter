import flask
from fga.frameworks.flask.flows import BeforeRequestFlow
from fga.settings import properties
from google.appengine.api import modules

import config

swagger_bp = flask.Blueprint('swagger', __name__, static_url_path='/swagger', static_folder='swagger', template_folder='swagger')
swagger_bp.before_request(BeforeRequestFlow(oauth_filter=False))

@swagger_bp.route('/ws-doc')
@swagger_bp.route('/ws-doc/')
@swagger_bp.route('/ws-doc/index.html')
def swagger_ui():
    print('enter to swagger')
    scheme = flask.request.scheme.lower()
    if modules.get_current_module_name() == "default":
        host = modules.get_hostname().split('.', 1)[-1].split('.',1)[-1]
    else:
        host = modules.get_hostname().split('.', 1)[-1].replace('.', '-dot-', 1)
    return flask.render_template('index.html', client_id=config.get_config().SWAGGER_UI_OAUTH_CLIENT_ID,
                                 url='{}://{}'.format(scheme, host))
