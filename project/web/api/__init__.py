import os

from flask import Flask


app = Flask(__name__,static_folder='static', static_url_path='/static')

app.secret_key = 'A0sdfhasd~Zr98j/3yX R~XHH!jmN]LWX/,?RF'


from . import views
from . import urls

if __name__ == '__main__':
    app.run()
