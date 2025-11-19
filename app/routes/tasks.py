from flask import Blueprint, render_template,redirect,request,url_for,flash,session
from app import db
from app.models import Task

task_bp = Blueprint('tasks',__name__)

@task_bp.route('/')
def view_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.filter_by(user_id = session['user_id']).all()
    return render_template('tasks.html',tasks = tasks)
@task_bp.route('/add',methods = ['POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        new_task = Task(title = title,status = 'Pending',user_id = session['user_id'])
        db.session.add(new_task)
        # It registers this object as something you want to insert later
        db.session.commit()
        flash('Task added successfully','success')
    return redirect(url_for('tasks.view_tasks'))

@task_bp.route('/toggle/<int:task_id>',methods = ['POST'])
def toggle_status(task_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    task = Task.query.filter_by(id = task_id,user_id = session['user_id']).first()
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status =='Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
            
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))
    
        
@task_bp.route('/clear',methods = ["POST"])
def clear_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    Task.query.filter_by(user_id=session['user_id']).delete()
    db.session.commit()
    flash('All tasks cleared')
    return redirect(url_for('tasks.view_tasks'))
    


# delete button
# multiple admin in sessions jo hum register kry gy
    
