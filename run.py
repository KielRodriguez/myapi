from datetime import datetime

from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

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


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parse = reqparse.RequestParser()
parse.add_argument('description', type=str, required=True)
parse.add_argument('quantity', type=int, required=True)
parse.add_argument('account', type=float, required=True)


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return EXPENSES[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del EXPENSES[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        EXPENSES[todo_id] = task
        return task, 201

# TodoList
# show a list of all todos, and lets you POS to add new tasks
class TodoList(Resource):
    def get(self):
        return EXPENSES

    def post(self):
        args = parse.parse_args()
        _id = max(EXPENSES.keys()) + 1

        EXPENSES[_id] = {
            'description': args['description'],
            'quantity': args['quantity'],
            'account': args['account'],
            'purchase_date': datetime.now().strftime("%d-%m-%Y")
        }

        return EXPENSES[_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
