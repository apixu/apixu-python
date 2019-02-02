import os
from dotenv import dotenv_values
import logging
from apixu.client import ApixuClient, ApixuException
from flask import Flask, request, jsonify

os.environ.update(dotenv_values())

api_key = os.environ['APIXUKEY']
client = ApixuClient(api_key)

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_invalid_usage(error):
    logging.exception(error)
    return jsonify({'error': 'Internal Server Error'}), 500


@app.errorhandler(ValueError)
def handle_invalid_usage(error):
    return jsonify({'error': str(error)}), 400


@app.errorhandler(ApixuException)
def handle_invalid_usage(error):
    if error.code != 1006:
        raise Exception(error)

    return jsonify({'error': 'Could not find location.'}), 404


@app.route('/weather', methods=['GET'])
def weather():
    query = request.args.get('q')
    if query is None or query.strip() == '':
        raise ValueError('Empty or missing query.')

    current = client.current(q=query)
    return jsonify(current)


if __name__ == '__main__':
    app.run()
