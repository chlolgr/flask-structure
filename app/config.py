import os
basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()


class Config(object): 
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.environ['SECRET_KEY']
