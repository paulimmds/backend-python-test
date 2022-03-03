from alayatodo._todo import todo_bp
from flask  import render_template, session, redirect, request
from alayatodo.models import Todo
from alayatodo import db

@todo_bp.route('/todo/<id>', methods=['GET'])
def todo(id):
    todo = Todo.query.filter_by(id=id).first()
    return render_template('todo.html', todo=todo)


@todo_bp.route('/todo', methods=['GET'])
@todo_bp.route('/todo/', methods=['GET'])
def todos():
    if not session.get('logged_in'):
        return redirect('/login')
    todos = Todo.query.all()
    return render_template('todos.html', todos=todos)


@todo_bp.route('/todo', methods=['POST'])
@todo_bp.route('/todo/', methods=['POST'])
def todos_POST():
    if not session.get('logged_in'):
        return redirect('/login')

    todo = Todo(user_id=session['user']['id'], description=request.form.get('description'))
    db.session.add(todo)
    db.session.commit()
    return redirect('/todo')


@todo_bp.route('/todo/<id>', methods=['POST'])
def todo_delete(id):
    if not session.get('logged_in'):
        return redirect('/login')

    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/todo')

