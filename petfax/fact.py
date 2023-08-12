import json 
from flask import ( Blueprint, render_template, request, redirect )

bp = Blueprint('fact', __name__, url_prefix="/facts")

pets = json.load(open('pets.json'))


@bp.route('/new')
def fax(): 
    return render_template('new.html')

@bp.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':
       print(request.form)
       return redirect('/facts')
    
    return render_template('facts/index.html')

