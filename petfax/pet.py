import json 
from flask import Blueprint, render_template 

bp = Blueprint('pet', __name__, url_prefix="/pets")

pets = json.load(open('pets.json'))

@bp.route('/')
def index(): 
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show(pet_id): 
    pet=pets[pet_id-1]
    return render_template('show.html', pet=pet)