import re
from flask import Flask, app, render_template
from flask.helpers import flash

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)