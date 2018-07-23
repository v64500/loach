# -*- coding: utf-8 -*-
from flask import Flask
from loach.api import douyin
from loach.setting import config
from loach.schedule import schedul


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # load extensions

    # load blueprints
    app.register_blueprint(douyin)

    return app


schedul.start()
app = create_app(config)
app.run(host='127.0.0.1', port=8080)

