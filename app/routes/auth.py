from flask import Blueprint, render_template,redirect,request,url_for,flash,session
from app.forms.login import LoginForm
from app.forms.register import RegisterForm


auth_bp = Blueprint('auth',__name__)

USER_CREDENTIALS = {
   'Waniya':'1234'
    
}

@auth_bp.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['user'] = username   
            flash('Login Succesfully','success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid username or password','danger sallla')
            
    return render_template('login.html',form = form)

@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('logged out','info')
    return redirect(url_for('auth.login'))
        
@auth_bp.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        USER_CREDENTIALS[username] = password
        flash('Registered Succesfully','success')
            
        return redirect(url_for('auth.login'))
        
            
    return render_template('register.html',form = form)
       
        