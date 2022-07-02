from flask import Flask, render_template, request, flash
app = Flask(__name__)

app.secret_key="a"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/glowna")
def glowna():
  
    return render_template("index.html")


@app.route("/funkcja")
def funkcja():
  
    return render_template("funkcja.html")

@app.route("/autorzy")
def autorzy():

    return render_template("autorzy.html")   



