from http import HTTPStatus

from flask import redirect, render_template
from werkzeug.exceptions import NotFound

from . import app
from .forms import URL_mapForm
from .models import URL_map


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    url_map = URL_map()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    url_map.create_short_url(form.original_link.data, form.custom_id.data)
    return render_template(
        'index.html',
        **{'form': form, 'url_map': url_map}
    )


@app.route('/<string:short>')
def url_map_view(short):
    url_map = URL_map()
    link = url_map.original_link(short=short)
    if not link:
        raise NotFound(
            'Указанный id не найден', HTTPStatus.NOT_FOUND)
    return redirect(link.original)
