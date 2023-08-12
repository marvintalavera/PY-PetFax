from flask import Flask 
from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)

        # database config 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:marvintalavera@localhost:5432/pet-fax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models 
    models.db.init_app(app) 
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app

