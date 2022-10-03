from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (DataRequired, Length,
                                Optional, Regexp,
                                URL, ValidationError)

from .models import URL_map


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 128),
            URL(require_tld=True, message=('Некорректный URL'))
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(
                r'^[A-Za-z0-9]+$',
                message='Допустимые символы [A-Za-z0-9]'
            )
        ]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if field.data and URL_map.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя {field.data} уже занято!')
