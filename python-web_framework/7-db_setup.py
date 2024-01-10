from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

############################# TO DO 1 ############################
# Configure Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
###################################################################

db = SQLAlchemy(app)

############################ TO DO 2 ##############################
# Define the User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
###################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    