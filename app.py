from datetime import datetime

from flask import Flask, request
from flask_restful import Api

from resources.expenditure import Expenditure

app = Flask(__name__)
api = Api(app)


##
## Actually setup the Api resource routing here
##
api.add_resource(Expenditure, '/expenses', '/expenses/<int:expenditure_id>')


if __name__ == '__main__':
    app.run(debug=True)
