import os

from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource
from flask_migrate import Migrate

from models import Dog, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app=app, db=db)
db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return {'msg': 'Welcome to the Dog API!'}

class Dogs(Resource):
    def get(self):
        dogs = [dog.to_dict() for dog in Dog.query.all()]
        return make_response(jsonify(dogs), 200)
    
api.add_resource(Dogs, '/dogs')