#!/usr/bin/python3
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                           states=states,
                           amenities=amenities)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
