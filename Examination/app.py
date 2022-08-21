from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# อ่านไฟล์
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystatement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)

# กำหนดค่าที่รับเข้ามา
class Statement(database.Model):
    name = database.Column(database.String(50), primary_key=True)
    team = database.Column(database.String(50), nullable=False)
    sex = database.Column(database.String(50), nullable=False)
    love = database.Column(database.String(50), nullable=False)
    score = database.Column(database.String(50), nullable=False)
    lost = database.Column(database.String(50), nullable=False)

# สร้างไฟล์
database.create_all()

# เพิ่มข้อมูล
@app.route("/addForm")
def addForm():
    return render_template("addForm.html")

# ส่งข้อมูลที่ได้มาเพิ่มลงไปใน database
@app.route("/addStatement", methods=['POST'])
def addStatement():
    name = request.form["name"]
    team = request.form["team"]
    sex = request.form["sex"]
    love = request.form["love"]
    score = request.form["score"]
    lost = request.form["lost"]
    statement = Statement(name=name, team=team, sex=sex, love=love, score=score, lost=lost)
    database.session.add(statement)
    database.session.commit()
    return redirect("/")

# แสดงข้อมูล
@app.route("/")
def showData():
    statements = Statement.query.all()
    return render_template("statements.html", statements=statements)

# ลบข้อมูล
@app.route("/delete/<string:name>")
def deleteStatement(name):
    statement = Statement.query.filter_by(name=name).first()
    database.session.delete(statement)
    database.session.commit()
    return redirect("/")

# แก้ไขข้อมูล
@app.route("/edit/<string:name>")
def editStatement(name):
    statement = Statement.query.filter_by(name=name).first()
    return render_template("editForm.html", statement=statement)

# อัพเดทข้อมูลที่ทำการแก้ไข
@app.route("/updateStatement", methods=['POST'])
def updateStatement():
    name = request.form["name"]
    team = request.form["team"]
    sex = request.form["sex"]
    love = request.form["love"]
    score = request.form["score"]
    lost = request.form["lost"]
    statement = Statement.query.filter_by(name=name).first()
    statement.name = name
    statement.team = team
    statement.sex = sex
    statement.love = love
    statement.score = score
    statement.lost = lost
    database.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
