from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Todo(db.Model):
    """Todo Model"""

    __tablename__="todos"
    id=db.Column(db.Integer, primary_key= True,autoincrement= True)
    content= db.Column(db.Text, nullable= False)
    category= db.Column(db.String)
    done=db.Column(db.Boolean, default= False)
    created_at = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def serialized(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done
        }

    def __repr__(self):
        return f"<Todo id={self.id} title={self.title} done=title={self.done} category={self.category}>"
   
   
