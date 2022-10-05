import random
from datetime import datetime
from string import ascii_letters, digits

from flask import url_for

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

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])

    def get_unique_short_id(self,
                            symbols=ascii_letters + digits,
                            id_length=6):
        random_value = ''.join(random.choice(symbols)
                               for _ in range(id_length))
        if URL_map.query.filter_by(short=random_value).first() is None:
            setattr(self, 'short', random_value)

    def create_short_url(self, original=None, short=None):
        if original == '' or original is None:
            raise ValueError('Отсутствует URL!')
        setattr(self, 'original', original)
        if short == '' or short is None:
            self.get_unique_short_id()
        else:
            if URL_map.query.filter_by(short=short).first():
                raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
            setattr(self, 'short', short)
        db.session.add(self)
        db.session.commit()

    def original_link(self, short):
        return URL_map.query.filter_by(short=short).first()
