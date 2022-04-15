from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', name="World")

@app.route("/<name>")
def hello_you(name):
    return render_template('index.html', name=name)
