from alayatodo._todo import todo_bp
from flask  import render_template, redirect, request, flash, url_for
from alayatodo.models import Todo
from alayatodo import db, login
from flask_login import login_required, current_user

@todo_bp.route('/todo/<id>', methods=['GET'])
@login_required
def todo(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo and current_user.id == todo.user_id:
        return render_template('todo.html', todo=todo)
    flash('Todo not exist!')
    return redirect('/todo')

@todo_bp.route('/todo/<id>/json', methods=['GET'])
@login_required
def todo_json(id):
    todo = Todo.query.get(id)
    if todo and current_user.id == todo.user_id:
        todo = {
            'id':todo.id,
            'user_id':todo.user_id,
            'description':todo.description
        }
        return todo
    flash('Todo does not exist.')
    return redirect('/')

@todo_bp.route('/todo/', methods=['GET'])
def todos():
    if not current_user.is_authenticated:
        return login.unauthorized(), 401

    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('todos.html', todos=todos)

@todo_bp.route('/todo/', methods=['POST'])
@login_required
def todos_POST():
    try:
        description = request.form.get('description')
        todo = Todo(user_id=current_user.id, description=description)
        db.session.add(todo)
        db.session.commit()
    except AssertionError as error:
        flash(error.args[0], 'danger')
        return redirect('/todo')
    
    flash("Success!!! You've added a new task to do!")
    return redirect('/todo')

@todo_bp.route('/todo/<id>', methods=['POST'])
@login_required
def todo_delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    flash("Success!!! You removed your task!")
    return redirect('/todo')

@todo_bp.route('/todo/<id>/status/', methods=['POST'])
@login_required
def todo_set_status(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.set_status()
    db.session.commit()
    next = request.args.get('next')
    if next:
        return redirect(url_for(next, id=id))
    return redirect('/todo')