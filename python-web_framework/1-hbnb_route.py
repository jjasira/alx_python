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

"""This will enable the app to be run by python"""
if __name__ == "__main__":
    """set the host and port"""
    app.run(host='0.0.0.0', port=5000)