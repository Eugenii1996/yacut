from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (DataRequired, Length,
                                Optional, Regexp,
                                URL, ValidationError)

from .constants import ORIGINAL_LEGTH, SHORT_LENGTH, VALID_SYMBOLS
from .models import URL_map


CREATE = 'Создать'
CUSTOM_SHORT_LINK = 'Ваш вариант короткой ссылки'
INVALID_URL = 'Некорректный URL'
LONG_LINK = 'Длинная ссылка'
NAME_USED = 'Имя {name} уже занято!'
REQUIRED_FIELD = 'Обязательное поле'
VALID_CHARACTERS = 'Допустимые символы [A-Za-z0-9]'


class URL_mapForm(FlaskForm):
    original_link = URLField(
        LONG_LINK,
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            Length(max=ORIGINAL_LEGTH),
            URL(require_tld=True, message=INVALID_URL)
        ]
    )
    custom_id = StringField(
        CUSTOM_SHORT_LINK,
        validators=[
            Length(max=SHORT_LENGTH),
            Optional(),
            Regexp(
                rf'^[{VALID_SYMBOLS}]+$',
                message=VALID_CHARACTERS
            )
        ]
    )
    submit = SubmitField(CREATE)

    def validate_custom_id(self, field):
        if field.data and URL_map.original_link(field.data):
            raise ValidationError(NAME_USED.format(name=field.data))
