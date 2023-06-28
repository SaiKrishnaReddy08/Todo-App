from flask import render_template, redirect, url_for,request
from todo_app import app,db
from todo_app.forms import addListForm,addTaskForm
from todo_app.models import Todolist,Task

@app.route('/', methods=['GET','POST'])
def home():
    listform = addListForm()
    if listform.validate_on_submit():
        with app.app_context():
            l = Todolist(name = listform.name.data)
            db.session.add(l)
            db.session.commit()
            listform.name.data=''
    return render_template('home.html', table1=Todolist, table2=Task, listform = listform)

@app.route('/addTask', methods=['GET','POST'])
def addTask():
    taskform = addTaskForm()
    all_lists=[]
    with app.app_context():
        for i in Todolist.query.all():
            all_lists.append(i.name)
    taskform.category.choices = all_lists    
    if taskform.validate_on_submit():
        with app.app_context():
            task = Task(work=taskform.work.data, due_date=taskform.due_date.data, category=taskform.category.data)
            db.session.add(task)
            lst = Todolist.query.filter_by(name=taskform.category.data).first()
            lst.finish_count+=1
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('addTask.html', taskform=taskform)

@app.route('/<list_name>', methods=['GET','POST'])
def show_works(list_name):
    listform = addListForm()
    if listform.validate_on_submit():
        with app.app_context():
            l = Todolist(name = listform.name.data)
            db.session.add(l)
            db.session.commit()
            listform.name.data=''
    
    lst = Todolist.query.filter_by(name=list_name).first()
    return render_template('show_works.html', lst=lst, table1=Todolist, table2=Task, listform = listform)

@app.route('/<int:task_id>')
def mark_done(task_id):
    with app.app_context():
        db.session.begin()
        t = Task.query.get(task_id)
        t.finished=True
        lst = Todolist.query.filter_by(name=t.category).first()
        lst.finish_count-=1
        db.session.commit()
    return redirect(request.referrer)

@app.route('/finished')
def finished():
    listform = addListForm()
    if listform.validate_on_submit():
        with app.app_context():
            l = Todolist(name = listform.name.data)
            db.session.add(l)
            db.session.commit()
            listform.name.data=''
    return render_template('finished.html', table1=Todolist, table2=Task, listform = listform)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    with app.app_context():
        t = Task.query.get(task_id)
        db.session.delete(t)
        db.session.commit()
    return redirect(url_for('finished'))