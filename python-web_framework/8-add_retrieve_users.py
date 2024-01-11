from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<db_username>:<db_password>@localhost/alx_flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

############################ TO DO 3 ##############################
# Implement a new route /add_user in your Flask application.
# Ensure this route handles both GET and POST requests.
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully!")
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", 'error')
    return render_template('add_user.html')
###################################################################

############################ TO DO 4 ##############################
# Create a new route /users.
# Connect to the alx_flask_db database and retrieve all users from the User table.
# Render the results using an HTML template (recommended file name: 8-users.html).
@app.route('/users', methods=['GET'])
def display_users():
    users = User.query.all()
    return render_template('users.html', users=users)
###################################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    