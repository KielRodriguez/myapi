from flask_restful import reqparse, abort, Resource

EXPENSES = {

    1: {  
        'description': 'luz', 
        'quantity': 1,
        'account': 100.0,
        'purchase_date': '01-12-2018'
    },
    2: {
        'description': 'garrafon epura', 
        'quantity': 1,
        'account': 40.0,
        'purchase_date': '01-12-2018'
    },
    3: {
        'description': 'articulos de limpieza', 
        'quantity': 1,
        'account': 45.3, 
        'purchase_date': '01-12-2018'
    }
}

# Function validate exist expenditure
def abort_if_expenditure_doesnt_exist(expenditure_id):
    if expenditure_id not in EXPENSES:
        abort(404, message="Expenditure {} doesn't exist".format(expenditure_id))

parse = reqparse.RequestParser()
parse.add_argument('description', type=str, required=True)
parse.add_argument('quantity', type=int, required=True)
parse.add_argument('account', type=float, required=True)

# Expenditure
# Show, update and delete a sigle expenditure. 
class Expenditure(Resource):
    def get(self, expenditure_id):
        abort_if_expenditure_doesnt_exist(expenditure_id)
        return EXPENSES[expenditure_id]


    def delete(self, expenditure_id):
        abort_if_expenditure_doesnt_exist(expenditure_id)
        del EXPENSES[expenditure_id]
        return '', 204

    def put(self, expenditure_id):
        args = parser.parse_args()
        EXPENSES[expenditure_id] = {
            'description': args['description'],
            'quantity': args['quantity'],
            'account': args['account']
        }

    def get(self):
        return EXPENSES

    
    def post(self):
        args = parse.parse_args()
        _id = max(EXPENSES.keys) + 1
        EXPENSES[_id] = {
            'description': args['description'],
            'quantity': args['quantity'],
            'account': args['account'],
            'purchase_date': args['purchase_date'],
        }

        return EXPENSES[_id], 201
