#!/usr/bin/python3
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    list_states = storage.all(State).values()
    return render_template("7-states_list.html", states=list_states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
