
from flask import Flask
from flask_seasurf import SeaSurf
from flask_cors import CORS
from flask_talisman import Talisman
from app.routes import *
from app.utils import CustomEncoder, CustomDecoder
from app import config


class MyFlaskApp(Flask):
    json_encoder = CustomEncoder
    json_decoder = CustomDecoder


def create_app() -> MyFlaskApp:
    newApp = MyFlaskApp(__name__)
    newApp.register_blueprint(home_route)
    newApp.register_blueprint(api_route)
    newApp.config.from_object(config)
    newApp.template_folder = "./template"
    newApp.static_folder = "./static"
    CORS(newApp)
    return newApp
