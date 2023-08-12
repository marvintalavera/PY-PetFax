import json 
from flask import Blueprint, render_template 

bp = Blueprint('fax', __name__, url_prefix="/fax")

pets = json.load(open('pets.json'))


@bp.route('/new')
def fax(): 
    return render_template('fax.html')

