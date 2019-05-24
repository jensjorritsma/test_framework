from flask import Flask, jsonify, request
from flask_accept import accept_fallback
from flask.logging import default_handler
import logging
framework = Flask(__name__)


@framework.route('/', methods=['GET', 'POST'])
@accept_fallback
def default_response():
    return '<p>Hello, World</p>'


@default_response.support('application/json')
def default_response_json():
    return jsonify(message="Good morning")


if __name__ == 'framework_app':
    if framework.debug:
        FORMAT = '%(asctime)s %(request.url)s'
        logging.basicConfig(format=FORMAT)
        logger = logging.getLogger()
        logger.debug()
