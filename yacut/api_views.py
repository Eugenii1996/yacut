from http import HTTPStatus
from string import ascii_letters, digits

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URL_map


SHORT_LENGTH = 6


@app.route('/api/id/<string:short_id>/')
def get_url(short_id):
    url_map = URL_map()
    link = url_map.original_link(short=short_id)
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
    output_data = [data['url']]
    url_map = URL_map()
    print(data)
    if ('custom_id' in data and
       data['custom_id'] != '' and
       data['custom_id'] is not None):
        custom_id = data['custom_id']
        for symbol in custom_id:
            if (symbol not in (ascii_letters + digits) or
               len(custom_id) > SHORT_LENGTH):
                raise InvalidAPIUsage(
                    'Указано недопустимое имя для короткой ссылки')
        output_data.append(data['custom_id'])
    url_map.create_short_url(*output_data)
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
