#!/usr/bin/python3
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html",
                           states=states,
                           amenities=amenities,
                           places=places)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
