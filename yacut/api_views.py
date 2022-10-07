from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URL_map


INVALID_SHORT_LINK = 'Указано недопустимое имя для короткой ссылки'
MISSING_REQUEST_BODY = 'Отсутствует тело запроса'
SHORT_ID_NOT_FOUND = 'Указанный id не найден'
URL_IS_REQUIRED_FIELD = '"url" является обязательным полем!'


@app.route('/api/id/<string:short_id>/')
def get_url(short_id):
    link = URL_map.original_link(short_id)
    if not link:
        raise InvalidAPIUsage(
            SHORT_ID_NOT_FOUND, HTTPStatus.NOT_FOUND)
    return jsonify({'url': link.original})


@app.route('/api/id/', methods=['POST'])
def add_url_map():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(MISSING_REQUEST_BODY)
    if 'url' not in data:
        raise InvalidAPIUsage(URL_IS_REQUIRED_FIELD)
    try:
        url_map = URL_map.create_short_url(data['url'], data.get('custom_id'))
    except ValueError:
        raise InvalidAPIUsage(INVALID_SHORT_LINK)
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
