# from app import create_app, db
# from app.models import User, Task

# app = create_app()

# with app.app_context():
#     db.create_all()   # <-- TABLES GET CREATED HERE

# if __name__ == "__main__":
#     app.run(debug=True)

from app import create_app, db
from app.models import User, Task

app = create_app()

# allow `flask shell` to auto-import db/User/Task
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Task': Task}

if __name__ == "__main__":
    app.run(debug=True)
