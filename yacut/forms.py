from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (DataRequired, Length,
                                Optional, Regexp,
                                URL, ValidationError)

from . import app
from .models import URL_map


CREATE = 'Создать'
INVALID_URL = 'Некорректный URL'
NAME_USED = 'Имя {name} уже занято!'
REQUIRED_FIELD = 'Обязательное поле'
VALID_CHARACTERS = 'Допустимые символы [A-Za-z0-9]'


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            Length(max=app.config['ORIGINAL_LEGTH']),
            URL(require_tld=True, message=INVALID_URL)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(max=app.config['SHORT_LENGTH']),
            Optional(),
            Regexp(
                # Не нашел как экранировать символы передаваемой константы
                rf'^[{app.config["VALID_SYMBOLS"]}]+$',
                message=VALID_CHARACTERS
            )
        ]
    )
    submit = SubmitField(CREATE)

    def validate_custom_id(self, field):
        if field.data and URL_map.original_link(field.data):
            raise ValidationError(NAME_USED.format(name=field.data))
