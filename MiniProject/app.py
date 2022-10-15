from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from calculateCar import Calculate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystatement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)
app.app_context().push()

class Statement(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), primary_key=False)
    date = database.Column(database.String(50), nullable=False)
    image = database.Column(database.String(50), nullable=False, default="default.jpg")
    phone = database.Column(database.String(50), nullable=False)
    car = database.Column(database.String(50), nullable=False)
    mesphone = database.Column(database.String(200), nullable=False)
    mescar = database.Column(database.String(200), nullable=False)
    positive_resultphone = database.Column(database.Integer, nullable=False)
    negative_resultphone = database.Column(database.Integer, nullable=False)
    positive_resultcar = database.Column(database.Integer, nullable=False)
    negative_resultcar = database.Column(database.Integer, nullable=False)

database.create_all()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/sendphone/<int:id>", methods=['POST'])
def sendphone(id):
    numberphone = request.form["numberphone"]
    #mesphone, positive_resultphone, negative_resultphone = Calculate.carnumber(numberphone)
    statement = Statement.query.filter_by(id=id).first()
    statement.phone  = numberphone
    statement.mesphone = "mesphone"
    statement.positive_resultphone = 50
    statement.negative_resultphone = 50
    database.session.commit()
    return redirect("/index/{0}".format(statement.id))

@app.route("/sendcar/<int:id>", methods=['POST'])
def sendcar(id):
    numbercar = request.form["numbercar"]
    mescar, positive_resultcar, negative_resultcar = Calculate.carnumber(numbercar)
    statement = Statement.query.filter_by(id=id).first()
    statement.car  = numbercar
    statement.mescar = mescar
    statement.positive_resultcar = positive_resultcar
    statement.negative_resultcar = negative_resultcar
    database.session.commit()
    return redirect("/index/{0}".format(statement.id))

def save_image(image_file):
    image_name = image_file.filename
    image_path = os.path.join(app.root_path, "static/profile_image", image_name)
    image_file.save(image_path)
    return image_name

@app.route("/addUser", methods=['POST'])
def addUser():
    name = request.form["name"]
    date = request.form["date"]
    file = request.files["image"]
    image_file = save_image(file)
    url_for("static", filename="profile_image/"+image_file)
    statement = Statement(name=name, date=date, image=file.filename, phone="", car="", mesphone="", mescar="", positive_resultphone=0, negative_resultphone=0, positive_resultcar=0, negative_resultcar=0)
    database.session.add(statement)
    database.session.commit()
    return redirect("/index/{0}".format(statement.id))

@app.route("/index/<int:id>")
def index(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("index.html", statement=statement)

@app.route("/dataDeveloper/<int:id>")
def dataDeveloper(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("dataDeveloper.html", statement=statement)

@app.route("/showData/<int:id>")
def showData(id):
    statement = Statement.query.filter_by(id=id).first()
    data = Statement.query.all()
    return render_template("showData.html", statement=statement, data=data)

@app.route("/relationship/<int:id>")
def relationship(id):
    statement = Statement.query.filter_by(id=id).first()
    data = Statement.query.all()
    return render_template("relationship.html", statement=statement, data=data)

if __name__ == "__main__":
    app.run(debug=True)