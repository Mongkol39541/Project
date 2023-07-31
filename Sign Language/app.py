from flask import Flask, render_template, Response
import cv2
from tensorflow.keras.models import load_model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dataDeveloper")
def dataDeveloper():
    return render_template("dataDeveloper.html")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")

if __name__=="__main__":
    app.run(debug=True)
