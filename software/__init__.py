from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'somethingonlymeknow'
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost:5432/blog_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.init_app(app)

    from .views import views

    app.register_blueprint(views)

    return app