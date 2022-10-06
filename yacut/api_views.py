from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URL_map


@app.route('/api/id/<string:short_id>/')
def get_url(short_id):
    link = URL_map.original_link(short_id)
    if not link:
        raise InvalidAPIUsage(
            'Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': link.original})


@app.route('/api/id/', methods=['POST'])
def add_url_map():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    original = data['url']
    if 'custom_id' in data:
        url_map = URL_map.create_short_url(original, data['custom_id'])
    else:
        url_map = URL_map.create_short_url(original)
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
