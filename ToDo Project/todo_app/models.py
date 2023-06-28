from todo_app import db

class Todolist(db.Model):
    name = db.Column(db.String(20),unique=True, nullable=False, primary_key=True)
    finish_count = db.Column(db.Integer(), default=0)
    works = db.relationship('Task', backref='listName', lazy=True)
    def __repr__(self):
        return f'Todolist({self.name})'
    
class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    work = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(), db.ForeignKey('todolist.name'), nullable=False)
    finished = db.Column(db.Boolean, default=False)
    def __repr__(self):
        return f'Todolist({self.work})'