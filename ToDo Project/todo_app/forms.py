from todo_app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField, SelectField
from wtforms.validators import DataRequired, ValidationError
from todo_app.models import Todolist

class addListForm(FlaskForm):
    name = StringField(label='List Name', validators=[DataRequired()] )

    def validate_name(self,field):
        with app.app_context():
            l = Todolist.query.filter_by(name=field.data).first()
            if l:
                raise ValidationError('Already Exists')
    

class addTaskForm(FlaskForm):  
    work = StringField(label='What is to be done?' )
    due_date = DateField(label='Due Date' )
    category = SelectField(label='Add to List')
    add = SubmitField(label='Add')

    def validate_work(self,field):
        if field.data=='' or len(field.data)<5:
            raise ValidationError('Enter the task to be done')
        