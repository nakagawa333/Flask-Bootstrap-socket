# -*- coding: utf-8 -*-
from flask import Flask,render_template

from flask_socketio import SocketIO,emit

app = Flask(__name__)

app.config['SECRET_KEY'] = "asbuicfbeygd837gdwudb"

socketio = SocketIO(app)

@app.route("/")
def index():
  return render_template("home.html")

@socketio.on("my event")
def handle_my_custom_event(json):
  print("recived something" + str( json ))
  socketio.emit("my response",json)

if __name__ == "__main__":
  socketio.run(app,debug=True,port='4000', host='0.0.0.0')