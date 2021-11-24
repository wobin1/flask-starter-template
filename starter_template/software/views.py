from flask import Blueprint
# from .models import name_of_model
from software import db

views = Blueprint('views', __name__)

@views.route('/')
def register():            
    return "Hello world"

