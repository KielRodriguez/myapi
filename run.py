from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

EXPENSES = {

    {
        '_id': 1,
        'description': 'luz', 
        'quantity': 1,
        'account': 100.0,
        'purchase_date': '01-12-2018'
    },
    {
        '_id': 2,
        'description': 'garrafon epura', 
        'quantity': 1,
        'account': 40.0,
        'purchase_date': '01-12-2018'
    },
    {
        '_id': 3,
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
parse.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# TodoList
# show a list of all todos, and lets you POS to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parse.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
