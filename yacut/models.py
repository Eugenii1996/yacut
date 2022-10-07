import random
from re import escape, sub
from datetime import datetime

from flask import url_for

from .constants import (
    CYCLE_ATTEMPT_NUMBER,
    RANDOM_SHORT_LENGTH,
    SHORT_LENGTH,
    VALID_SYMBOLS
)
from yacut import db
from .error_handlers import InvalidAPIUsage


NAME_USED = 'Имя "{name}" уже занято.'
NOT_FIND_SHORT_URL = 'Не удалось подобрать короткий url!'
WRONG_SYMBOLS = 'Неподходящие символы: {symbols}'
WRONG_SHORT_LENGTH = (
    'Размер короткой ссылки {short_length} '
    'больше допустимого {short_max}'
)


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

    @staticmethod
    def get_unique_short_id(
        symbols=VALID_SYMBOLS,
        short_length=RANDOM_SHORT_LENGTH
    ):
        for _ in range(CYCLE_ATTEMPT_NUMBER):
            random_value = ''.join(random.choices(symbols, k=short_length))
            if not URL_map.original_link(random_value):
                return random_value
        raise ValueError(NOT_FIND_SHORT_URL)

    @staticmethod
    def create_short_url(original, short=None, validated_form=False):
        if short == '' or short is None:
            short = URL_map.get_unique_short_id()
        elif not validated_form:
            if len(short) > SHORT_LENGTH:
                raise ValueError(
                    WRONG_SHORT_LENGTH.format(
                        short_length=len(short),
                        short_max=SHORT_LENGTH
                    )
                )
            wrong_symbols = sub(rf'[{escape(VALID_SYMBOLS)}]', '', short)
            if wrong_symbols != '':
                raise ValueError(
                    WRONG_SYMBOLS.format(symbols=" ".join(set(wrong_symbols)))
                )
            if URL_map.original_link(short):
                raise InvalidAPIUsage(NAME_USED.format(name=short))
        url_map = URL_map(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @staticmethod
    def original_link(short):
        return URL_map.query.filter_by(short=short).first()

    @staticmethod
    def original_link_or_404(short):
        return URL_map.query.filter_by(short=short).first_or_404().original
