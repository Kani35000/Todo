from models import db, connect_db, Todo
from app import app

db.drop_all()
db.create_all()


todo1=Todo(title='feed the Chickens')
todo2=Todo(title='Water Orchids')
todo3=Todo(title='Wash dishes', done=True)
todo4=Todo(title='No but really, work out today!', done=True)
todo5=Todo(title='Collect eggs from chicken (steal thier unborn babies)')


db.session.add(todo1)
db.session.add(todo2)
db.session.add(todo3)
db.session.add(todo4)
db.session.add(todo5)
db.session.commit()

