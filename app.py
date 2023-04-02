from flask import Flask, request, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Todo

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///restful_todo_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']='TDjakes35'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():   
    todos= Todo.query.all()
    return render_template('todo2.html', todos=todos)


@app.route('/', methods = ['POST'])
def create_todo():
    content= request.form.get("content")
    category= request.form.get("category")
    todos= Todo.query.all()
    new_todo= Todo(content= content, category= category)
    db.session.add(new_todo)
    db.session.commit()
    return render_template('todo2.html', todos=todos, new_todo= new_todo)


@app.route('/api/todos')
def list_todos():
    all_todos= [todo.serialized() for todo in Todo.query.all()]
    return jsonify(todos=all_todos)

@app.route('/api/todos')
def get_todo(id):
    todo= Todo.query.get_or_404(id)
    return jsonify(todo=todo.serialized())

@app.route('/api/todos', methods=["POST"])
def create_todo_api():
    new_todo= Todo(title=request.json['title'])
    db.session.add(new_todo)
    db.session.commit()
    response_json= jsonify(todo=new_todo.serialized())
    return (response_json, 201) 

@app.route('/api/todos/<int:id>', methods=["PATCH"])
def update_todo_api(id):
    todo= Todo.query.get_or_404(id)
    todo.title=request.json.get['title',todo.title]
    todo.done=request.json.get['done',todo.done]
    db.session.commit()
    
    return jsonify(todo=todo.serialized()) 

@app.route('/api/todos/<int:id>', methods=["DELETE"])
def delete_todo(id):
    todo= Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    
    return jsonify(message='deleted') 


