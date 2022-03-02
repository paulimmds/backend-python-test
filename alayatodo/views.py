from alayatodo import app
from flask import (
    g,
    redirect,
    render_template,
    request,
    session
    )


@app.route('/')
def home():
    with app.open_resource('../README.md', mode='r') as f:
        readme = f.read()
        return render_template('index.html', readme=readme)


from alayatodo._auth import routes

@app.route('/todo/<id>', methods=['GET'])
def todo(id):
    cur = g.db.execute("SELECT * FROM todos WHERE id ='%s'" % id)
    todo = cur.fetchone()
    return render_template('todo.html', todo=todo)


@app.route('/todo', methods=['GET'])
@app.route('/todo/', methods=['GET'])
def todos():
    if not session.get('logged_in'):
        return redirect('/login')
    cur = g.db.execute("SELECT * FROM todos")
    todos = cur.fetchall()
    return render_template('todos.html', todos=todos)


@app.route('/todo', methods=['POST'])
@app.route('/todo/', methods=['POST'])
def todos_POST():
    if not session.get('logged_in'):
        return redirect('/login')
    g.db.execute(
        "INSERT INTO todos (user_id, description) VALUES ('%s', '%s')"
        % (session['user']['id'], request.form.get('description', ''))
    )
    g.db.commit()
    return redirect('/todo')


@app.route('/todo/<id>', methods=['POST'])
def todo_delete(id):
    if not session.get('logged_in'):
        return redirect('/login')
    g.db.execute("DELETE FROM todos WHERE id ='%s'" % id)
    g.db.commit()
    return redirect('/todo')
