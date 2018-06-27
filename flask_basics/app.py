#-*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__) #soble guion bajo son variables especiales

@app.route("/")#esto es un decorador
def index():
    return "Exto es una página index"

@app.route("/info")
def info():
     return "Info page"

@app.route("/profile")
def profile():
    return "Cesar Navarro"

@app.route("/about")
def about():
    return "<html><h1>QUIERES SABER MAS ACERCA DE NOSOTROS:<h1></html>"

#guard
if __name__ == '__main__':
    app.run(debug=True)
