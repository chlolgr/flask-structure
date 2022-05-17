from app import db


class Item(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer,primary_key=True)