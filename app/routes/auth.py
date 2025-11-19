from flask import Blueprint, render_template,redirect,request,url_for,flash,session
from app.forms.login import LoginForm
from app.forms.register import RegisterForm
from app.models import User
from app import db


auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session['user_id'] = user.id   
            flash('Login Succesfully','success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid username or password','danger sallla')
            
    return render_template('login.html',form = form)

@auth_bp.route('/logout')
def logout():
    session.pop('user_id',None)
    flash('logged out','info')
    return redirect(url_for('auth.login'))
        
@auth_bp.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_User = User(username = username,password = password)
        db.session.add(new_User)
        db.session.commit()
        
        flash('Registered Succesfully','success')
            
        return redirect(url_for('auth.login'))
        
            
    return render_template('register.html',form = form)
       
        