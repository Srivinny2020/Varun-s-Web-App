from flask import Flask
from config import config_options

def create_app(config_name):
	app = Flask(_name_)
	
	app.config.from_object(config_options[config.name])
	
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	from .requests import configure_requests
	configure_requests(app)
	
	return app
