"""Import the required files"""
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
"""Get the command line arguments and assign them to the variables"""
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
"""connect to the database"""
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"
###############################################################


db = SQLAlchemy(app)

############################  TO DO 2 ##############################
"""create the schema for the User"""
class User(db.Model):
    """These columns will be in the user table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
#################################################################

# Create the database tables

"""create the database tables using this function in the correct context"""
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables

"""This is our root route"""
@app.route('/', strict_slashes=False)
def index():
    """This will be returned in our home page"""
    return "Hello, ALX Flask!"

"""This is our add user route"""
@app.route('/add_user', methods=['GET', 'POST'], strict_slashes=False)
def add_user():
    """Action if its a POST request"""
    if request.method == 'POST':
        """code for handling POST request"""
        name = request.form.get('name')
        email = request.form.get('email')

        try:
            """Adding the new user to the database"""
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash("User added succefully!")
        except Exception as e:
            """handling the errors"""
            flash(f"Error: {str(e)}")

        return render_template('add_user.html')
    elif request.method == 'GET':
        name = request.form.get('name')

        try:
            single_user = User.query.filter_by(name=name).first()
        except Exception as e:
            """handling the errors"""
            flash(f"Error: {str(e)}")
        return render_template('add_user.html', single_user=single_user)

""" Retrieve Users Route:"""
@app.route('/users')
def show_users():
    """ Retrieve Users Route"""
    users = User.query.all()
    """Render the users in users.html"""
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)