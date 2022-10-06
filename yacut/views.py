from flask import redirect, render_template

from . import app
from .forms import URL_mapForm
from .models import URL_map


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    original = form.original_link.data
    if original == '' or original is None:
        raise ValueError('Отсутствует URL!')
    if 'custom_id' in form.data:
        url_map = URL_map.create_short_url(original, form.custom_id.data)
    else:
        url_map = URL_map.create_short_url(original)
    return render_template('index.html', form=form, url_map=url_map)


@app.route('/<string:short>')
def url_map_view(short):
    return redirect(URL_map.original_link_or_404(short))
