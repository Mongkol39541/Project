from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from calculateCar import carnumber, percarnumber
from calculateDay import calculateday
from calculateHouse import calculatehouse
from calculatePhone import phonenumber
import pandas as pd

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
    price = database.Column(database.String(50), nullable=False)
    car = database.Column(database.String(50), nullable=False)
    date = database.Column(database.String(50), nullable=False)
    house = database.Column(database.String(50), nullable=False)
    sumphone = database.Column(database.String(50), nullable=False)
    sumhouse = database.Column(database.String(50), nullable=False)
    mesphone = database.Column(database.String(200), nullable=False)
    mescar = database.Column(database.String(200), nullable=False)
    mesday = database.Column(database.String(200), nullable=False)
    mesmonth = database.Column(database.String(200), nullable=False)
    meshouse = database.Column(database.String(200), nullable=False)
    double_num = database.Column(database.String(200), nullable=False)
    mean_duo_af = database.Column(database.String(200), nullable=False)
    category = database.Column(database.String(200), nullable=False)
    positive_resultphone = database.Column(database.Integer, nullable=False)
    negative_resultphone = database.Column(database.Integer, nullable=False)
    positive_resultcar = database.Column(database.Integer, nullable=False)
    negative_resultcar = database.Column(database.Integer, nullable=False)
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
    try:
        sumphone, mesphone, positive_resultphone, negative_resultphone, double_num, mean_duo_af, category = phonenumber(numberphone)
        statement.sumphone = sumphone
        statement.phone  = numberphone
        statement.mesphone = mesphone
        statement.mesphone = mesphone
        statement.double_num = double_num
        statement.mean_duo_af = mean_duo_af
        statement.category = category
        statement.positive_resultphone = positive_resultphone
        statement.negative_resultphone = negative_resultphone
        database.session.commit()
        return redirect("/predictPhone/{0}".format(statement.id))
    except:
        return redirect("/index/{0}".format(statement.id))

@app.route("/sendcar/<int:id>", methods=['POST'])
def sendcar(id):
    numbercar = request.form["numbercar"]
    statement = Statement.query.filter_by(id=id).first()
    try:
        mescar = carnumber(numbercar)
        positive_resultcar, negative_resultcar = percarnumber(numbercar)
        statement.car  = numbercar
        statement.mescar = mescar
        statement.positive_resultcar = positive_resultcar
        statement.negative_resultcar = negative_resultcar
        database.session.commit()
        return redirect("/predictCar/{0}".format(statement.id))
    except:
        return redirect("/index/{0}".format(statement.id))

@app.route("/senddate/<int:id>", methods=['POST'])
def senddate(id):
    numberdate = request.form["numberdate"]
    statement = Statement.query.filter_by(id=id).first()
    try:
        mesday, mesmonth = calculateday.daynumber(numberdate)
        statement.date  = numberdate
        statement.mesday = mesday
        statement.mesmonth = mesmonth
        database.session.commit()
        return redirect("/predictDate/{0}".format(statement.id))
    except:
        return redirect("/index/{0}".format(statement.id))

@app.route("/sendhouse/<int:id>", methods=['POST'])
def sendhouse(id):
    numberhouse = request.form["numberhouse"]
    statement = Statement.query.filter_by(id=id).first()
    try:
        sumhouse, meshouse = calculatehouse.housenumber(numberhouse)
        statement.sumhouse = sumhouse
        statement.house  = numberhouse
        statement.meshouse = meshouse
        statement.positive_resulthouse = 50
        statement.negative_resulthouse = 50
        database.session.commit()
        return redirect("/predictHouse/{0}".format(statement.id))
    except:
        return redirect("/index/{0}".format(statement.id))

def save_image(image_file):
    image_name = image_file.filename
    image_path = os.path.join(app.root_path, "static/profile_image", image_name)
    image_file.save(image_path)
    return image_name

def splitdata(data):
    data = data[:len(data ) - 1].split(" ")
    return data

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
    statement = Statement(name=name, password=password, image=file.filename, phone="", price=0, car="", date="", house="", sumphone='', sumhouse='',mesphone="", mescar="", mesday="", mesmonth="", meshouse="", double_num='', mean_duo_af='', category='',positive_resultphone=0, negative_resultphone=0, positive_resultcar=0, negative_resultcar=0, total_positive=0)
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
    double_num = statement.double_num
    mean_duo_af = statement.mean_duo_af
    category = category = statement.category
    double_num = splitdata(double_num)
    mean_duo_af = splitdata(mean_duo_af)
    category = splitdata(category)
    data2D = []
    for loop in range(len(double_num)):
        data = {'double_num':double_num[loop], 'mean_duo_af':mean_duo_af[loop]}
        data2D.append(data)
    return render_template("predictPhone.html", statement=statement, data=data2D, categories=category)

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

@app.route("/showData<int:select>/<int:id>")
def showData(id, select):
    statement = Statement.query.filter_by(id=id).first()
    total = (statement.positive_resultphone + statement.positive_resultcar) / 2
    statement.total_positive = total
    database.session.commit()
    data = Statement.query.all()
    number = []
    top = 0
    datatop = []
    for num in data:
        number.append(num.total_positive)
    number.sort(reverse=True)
    for che in number:
        newdata = []
        top += 1
        for txt in range(len(data)):
            if data[txt].total_positive == che:
                value = data.pop(txt)
                if value.id == id:
                    unit = top
                newdata.append(value)
                newdata.append(top)
                break
        datatop.append(newdata)
    return render_template("showData.html", statement=statement, data=datatop[select - 100:select], unit=unit)

@app.route("/relationship/<int:id>")
def relationship(id):
    statement = Statement.query.filter_by(id=id).first()
    data_category = pd.read_csv('counts_category.csv')
    data_double = pd.read_csv('counts_double.csv')
    name_category = ''
    num_category = []
    price_category = []
    for loop_category in range(len(data_category.counts)):
        name_category += data_category.category[loop_category] + " "
        num_category.append(data_category.counts[loop_category])
        price_category.append(data_category.price[loop_category] // data_category.counts[loop_category])
    name_double = ''
    num_double = []
    price_double = []
    for loop_double in range(len(data_double.counts)):
        name_double += str(data_double.double[loop_double]) + " "
        num_double.append(data_double.counts[loop_double])
        price_double.append(data_double.price[loop_double] // data_double.counts[loop_double])
    return render_template("relationship.html", statement=statement, name_category=name_category, num_category=num_category, price_category=price_category, name_double=name_double, price_double=price_double)

if __name__ == "__main__":
    app.run(debug=True)