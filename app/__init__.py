from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#created database object globally
# You are creating a database object. But right now → it is empty, not connected to any Flask app.
db = SQLAlchemy()


# You are creating a function that will build and return the Flask app object.
def create_app():
    app = Flask(__name__) # flask app k instance
    # A secret key used by Flask to:protect sessions,protect cookies,protect CSRF tokens (forms protection)
    app.config['SECRET_KEY'] = 'waniya-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    # Use SQLite database named todo.db and store it in project folder.
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    
    # to connect db to app
    db.__init__(app)
    
    from app.routes.auth import auth_bp
    from app.routes.auth import task_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    # Add all task/auth routes to my main Flask application
    # mini app ki tarah related routes 
    return app
    
    
    