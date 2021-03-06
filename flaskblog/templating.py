from datetime import datetime

from flask import request
from jinja2 import Markup
from slugify import slugify

from .md import markdown
from .models import Category

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


def date(s, format='%Y-%m-%d'):
    return s.strftime(format)


def get_current_time():
    return {'current_time': datetime.now()}


def blog_objects():
    url = request.url
    title = request.url_rule.endpoint if request.url_rule else ''
    categories = Category.query.filter(Category.text != 'About').all()
    rv = {'url': url, 'title': title.title()}
    return {'page': rv, 'urljoin': urljoin, 'categories': categories}


def make_slugify(s):
    return slugify(s)


def render_markdown(s):
    return Markup(markdown(s))


def init_app(app):
    app.add_template_filter(date)
    app.add_template_filter(make_slugify, 'slugify')
    app.add_template_filter(render_markdown, 'render')
    app.context_processor(get_current_time)
    app.context_processor(blog_objects)
