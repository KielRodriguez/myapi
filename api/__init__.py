from flask_restful import Api

from app import app
from api.resources.expenditure import Expenditure

api = Api(app)

api.add_resource(Expenditure, '/expenditure')