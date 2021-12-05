from software import db
from datetime import datetime


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	author = db.Column(db.String(100), nullable=False)
	content = db.Column(db.String(2000), nullable=False)
	created_date = db.Column(db.DateTime, default=datetime.utcnow)




	


    