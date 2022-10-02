import os
from flask import Flask
from application.config import Config

app = Flask(__name__, template_folder = "templates")
app.config.from_object(Config)
app.app_context().push()
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    from application.controllers import *
    app.run(port = 4555)
