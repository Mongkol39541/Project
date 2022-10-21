from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from calculateCar import Calculate
from project2 import acx

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystatement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)
app.app_context().push()

class Statement(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), primary_key=False)
    password = database.Column(database.String(50), primary_key=False)
    image = database.Column(database.String(50), nullable=False, default="default.jpg")
    phone = database.Column(database.String(50), nullable=False)
    car = database.Column(database.String(50), nullable=False)
    date = database.Column(database.String(50), nullable=False)
    house = database.Column(database.String(50), nullable=False)
    mesphone = database.Column(database.String(200), nullable=False)
    mescar = database.Column(database.String(200), nullable=False)
    mesdate = database.Column(database.String(200), nullable=False)
    meshouse = database.Column(database.String(200), nullable=False)
    positive_resultphone = database.Column(database.Integer, nullable=False)
    negative_resultphone = database.Column(database.Integer, nullable=False)
    positive_resultcar = database.Column(database.Integer, nullable=False)
    negative_resultcar = database.Column(database.Integer, nullable=False)
    positive_resultdate = database.Column(database.Integer, nullable=False)
    negative_resultdate = database.Column(database.Integer, nullable=False)
    positive_resulthouse = database.Column(database.Integer, nullable=False)
    negative_resulthouse = database.Column(database.Integer, nullable=False)
    total_positive = database.Column(database.Integer, nullable=False)

database.create_all()

@app.route("/")
def singup():
    return render_template("singup.html", mes="", color="light")

@app.route("/login")
def login():
    return render_template("login.html", mes="", color="light")

@app.route("/sendphone/<int:id>", methods=['POST'])
def sendphone(id):
    numberphone = request.form["numberphone"]
    statement = Statement.query.filter_by(id=id).first()
    while not(numberphone.isnumeric()) or not(len(numberphone) == 10):
        statement.phone  = ""
        statement.mesphone = "Please Enter numeric only and full number."
        statement.positive_resultphone = 0
        statement.negative_resultphone = 0
        database.session.commit()
        return redirect("/index/{0}".format(statement.id))
    mesphone, positive_resultphone, negative_resultphone = acx.main(numberphone)
    statement.phone  = numberphone
    statement.mesphone = mesphone
    statement.positive_resultphone = positive_resultphone
    statement.negative_resultphone = negative_resultphone
    database.session.commit()
    return redirect("/predictPhone/{0}".format(statement.id))

@app.route("/sendcar/<int:id>", methods=['POST'])
def sendcar(id):
    numbercar = request.form["numbercar"]
    statement = Statement.query.filter_by(id=id).first()
    while not(numbercar.isnumeric()) or not(len(numbercar) == 4):
        statement.car  = ""
        statement.mescar = "Please Enter numeric only and full number."
        statement.positive_resultcar = 0
        statement.negative_resultcar = 0
        database.session.commit()
        return redirect("/index/{0}".format(statement.id))
    mescar, positive_resultcar, negative_resultcar = Calculate.carnumber(numbercar)
    statement.car  = numbercar
    statement.mescar = mescar
    statement.positive_resultcar = positive_resultcar
    statement.negative_resultcar = negative_resultcar
    database.session.commit()
    return redirect("/predictCar/{0}".format(statement.id))

@app.route("/senddate/<int:id>", methods=['POST'])
def senddate(id):
    numberdate = request.form["numberdate"]
    statement = Statement.query.filter_by(id=id).first()
    while not(numberdate.isnumeric()) or not(len(numberdate) == 6):
        statement.date  = ""
        statement.mesdate = "Please Enter numeric only and full number."
        statement.positive_resultdate = 0
        statement.negative_resultdate = 0
        database.session.commit()
        return redirect("/index/{0}".format(statement.id))
    #mesdate, positive_resultdate, negative_resultdate = Calculate.carnumber(numberdate)
    statement.date  = numberdate
    statement.mesdate = "mesdate"
    statement.positive_resultdate = 50
    statement.negative_resultdate = 50
    database.session.commit()
    return redirect("/predictDate/{0}".format(statement.id))

@app.route("/sendhouse/<int:id>", methods=['POST'])
def sendhouse(id):
    numberhouse = request.form["numberhouse"]
    statement = Statement.query.filter_by(id=id).first()
    while not(numberhouse.isnumeric()) or not(len(numberhouse) == 4):
        statement.house  = ""
        statement.meshouse = "Please Enter numeric only and full number."
        statement.positive_resulthouse = 0
        statement.negative_resulthouse = 0
        database.session.commit()
        return redirect("/index/{0}".format(statement.id))
    #meshouse, positive_resulthouse, negative_resulthouse = Calculate.carnumber(numberhouse)
    statement.house  = numberhouse
    statement.meshouse = "meshouse"
    statement.positive_resulthouse = 50
    statement.negative_resulthouse = 50
    database.session.commit()
    return redirect("/predictHouse/{0}".format(statement.id))

def save_image(image_file):
    image_name = image_file.filename
    image_path = os.path.join(app.root_path, "static/profile_image", image_name)
    image_file.save(image_path)
    return image_name

@app.route("/addUser", methods=['POST'])
def addUser():
    name = request.form["name"]
    password = request.form["password"]
    file = request.files["image"]
    if len(name) == 0 or len(password) == 0:
        mes = "กรุณากรอกข้อมูลชื่อผู้ใช้หรือรหัสผ่านให้ครบถ้วน"
        color = "danger"
        return render_template("singup.html", mes=mes, color=color)
    try:
        image_file = save_image(file)
        url_for("static", filename="profile_image/"+image_file)
    except:
        file.filename = "profile.jpg"
    statement = Statement(name=name, password=password, image=file.filename, phone="", car="", date="", house="",mesphone="", mescar="", mesdate="", meshouse="",positive_resultphone=0, negative_resultphone=0, positive_resultcar=0, negative_resultcar=0, positive_resultdate=0, negative_resultdate=0, positive_resulthouse=0, negative_resulthouse=0, total_positive=0)
    database.session.add(statement)
    database.session.commit()
    return redirect("/index/{0}".format(statement.id))

@app.route("/intoUser", methods=['POST'])
def intoUser():
    che = False
    name = request.form["name"]
    password = request.form["password"]
    statement = Statement.query.all()
    for sta in statement:
        if name == sta.name and password == sta.password:
            che = True
            return redirect("/index/{0}".format(sta.id))
    if che == False:
        mes = "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"
        color = "danger"
        return render_template("login.html", mes=mes, color=color)

@app.route("/index/<int:id>")
def index(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("index.html", statement=statement)

@app.route("/predictPhone/<int:id>")
def predictPhone(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("predictPhone.html", statement=statement)

@app.route("/predictCar/<int:id>")
def predictCar(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("predictCar.html", statement=statement)

@app.route("/predictDate/<int:id>")
def predictDate(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("predictDate.html", statement=statement)

@app.route("/predictHouse/<int:id>")
def predictHouse(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("predictHouse.html", statement=statement)

@app.route("/dataDeveloper/<int:id>")
def dataDeveloper(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("dataDeveloper.html", statement=statement)

@app.route("/showData/<int:id>")
def showData(id):
    statement = Statement.query.filter_by(id=id).first()
    total = (statement.positive_resultphone + statement.positive_resultcar + statement.positive_resultdate + statement.positive_resulthouse) / 4
    statement.total_positive = total
    database.session.commit()
    data = Statement.query.all()
    newdata = []
    number = []
    for num in data:
        number.append(num.total_positive)
    number.sort(reverse=True)
    for che in number:
        for txt in range(len(data)):
            if data[txt].total_positive == che:
                value = data.pop(txt)
                newdata.append(value)
                break
    return render_template("showData.html", statement=statement, data=newdata)

@app.route("/relationship/<int:id>")
def relationship(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("relationship.html", statement=statement)

if __name__ == "__main__":
    app.run(debug=True)