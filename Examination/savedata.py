import sqlite3 as It

class SaveData:
    def __init__(self, name, team, sex, love, score, lost):
        # อ่านไฟล์ และรับข้อมูล
        con = It.connect('mystatement.db')
        self.name = name
        self.team = team
        self.sex = sex
        self.love = love
        self.score = score
        self.lost = lost
        with con:
            # อัพเดทข้อมูล
            cur = con.cursor()
            cur.execute("insert into statement values('{0}', '{1}', '{2}', '{3}', {4}, '{5}')".format(self.name, self.team, self.sex, self.love, self.score, self.lost))
            #cur.execute("create table stu(name text, team text, sex text, love text, score int, wrong list)")
        con.close()
