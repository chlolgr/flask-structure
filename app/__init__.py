import flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import sqlalchemy.dialects.sqlite

app = flask.Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes,models