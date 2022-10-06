import random
from datetime import datetime

from flask import url_for

from . import app
from yacut import db
from .error_handlers import InvalidAPIUsage


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'url_map_view', short=self.short, _external=True))

    def get_unique_short_id(
        self,
        symbols=app.config['VALID_SYMBOLS'],
        short_length=app.config['RANDOM_SHORT_LENGTH']
    ):
        random_value = ''.join(random.choices(symbols, k=short_length))
        if URL_map.original_link(random_value):
            self.get_unique_short_id()
        return random_value

    @staticmethod
    def create_short_url(original, short=None):
        url_map = URL_map()
        if short == '' or short is None:
            url_map.short = url_map.get_unique_short_id()
        else:
            for symbol in short:
                if (symbol not in app.config['VALID_SYMBOLS'] or
                   len(short) > app.config['SHORT_LENGTH']):
                    raise InvalidAPIUsage(
                        'Указано недопустимое имя для короткой ссылки')
            if URL_map.query.filter_by(short=short).first():
                raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
            url_map.short = short
        url_map.original = original
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @staticmethod
    def original_link(short):
        return URL_map.query.filter_by(short=short).first()

    @staticmethod
    def original_link_or_404(short):
        return URL_map.query.filter_by(short=short).first_or_404().original
