"""We will import Flask from flask"""
from flask import Flask

"""This is tha name of the flask app"""
app = Flask(__name__)

"""This is the route definition"""
@app.route("/", strict_slashes=False)
def hello_world():
    """This is what will be returned from our route"""
    return "Hello HBNB!"

"""This is the route definition"""
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This is what will be returned from our route"""
    return "HBNB"

"""This route will display C plus the variable"""
@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """We will remove the _ and replace it with a space"""
    new_text = text.replace('_', ' ')
    """We will return the new text"""
    return 'C {}'.format(new_text)




"""This route will display python plus the variable"""
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """We will remove the _ and replace it with a space"""
    formatted_text = text.replace('_', ' ')
    """We will return the new text"""
    return f'Python {formatted_text}'


"""This will enable the app to be run by python"""
if __name__ == "__main__":
    """set the host and port"""
    app.run(host='0.0.0.0', port=5000)