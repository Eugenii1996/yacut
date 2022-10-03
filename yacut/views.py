import random
import string

from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URL_mapForm
from .models import URL_map


def get_unique_short_id():
    return ''.join(random.choice(
        string.ascii_letters + string.digits
    ) for i in range(6))


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        url_map = URL_map(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        flash(url_for('url_map_view', short=short, _external=True))
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def url_map_view(short):
    return redirect(
        URL_map.query.filter_by(short=short).first_or_404().original
    )
