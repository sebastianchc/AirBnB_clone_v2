#!/usr/bin/python3
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    states = storage.all(State).values()
    if id is None:
        return render_template("9-states.html", states=states, id=id)
    for state in states:
        if state.id == id:
            states = state.cities
            return render_template("9-states.html", states=states, id=state)
    return render_template("9-states.html", id=-1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
