
from flask_wordcloud.settings import *
from flask import redirect , render_template, url_for
from flask_wordcloud.views import home_view

@app.route('/', methods=['GET', 'POST'])
def home():
    return home_view()
