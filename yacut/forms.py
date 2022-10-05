from string import ascii_letters, digits

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (DataRequired, Length,
                                Optional, Regexp,
                                URL, ValidationError)

from .models import URL_map


MAX_LEGTH_ORIGINAL = 2000
MAX_LEGTH_CUSTOM = 16
SYMBOLS = ascii_letters + digits
REQUIRED_FIELD = 'Обязательное поле'
INVALID_URL = 'Некорректный URL'
VALID_CHARACTERS = 'Допустимые символы [A-Za-z0-9]'
NAME_USED = 'Имя {name} уже занято!'


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            Length(max=MAX_LEGTH_ORIGINAL),
            URL(require_tld=True, message=INVALID_URL)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(max=MAX_LEGTH_CUSTOM),
            Optional(),
            Regexp(
                rf'^[{SYMBOLS}]+$',
                message=VALID_CHARACTERS
            )
        ]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        url_map = URL_map()
        if field.data and url_map.original_link(short=field.data):
            raise ValidationError(NAME_USED.format(name=field.data))
