from tkinter import *
from tkinter import ttk
from controller import Controller
from data import choice_data
from savedata import SaveData

THEME_APP = '#375362'

class UserInterface:
    def __init__(self, controller:Controller):
        # กำหนดค่าเริ่มต้น
        self.controller = controller
        self.total = 0
        self.keepfalse = []
        # สร้างหน้าต่าง login เข้าสู่ระบบ
        self.window = Tk()
        self.window.title("โปรแกรมทำข้อสอบ")
        self.window.geometry("600x670")
        self.window.config(bg=THEME_APP)
        self.name_label = Label(text="ชื่อตัวละคร", fg="white", bg=THEME_APP, font=('Arial', 16, 'bold'))
        self.name_label.place(x=100, y=100)
        self.team_label = Label(text="สังกัดแก๊ง", fg="white", bg=THEME_APP, font=('Arial', 16, 'bold'))
        self.team_label.place(x=100, y=200)
        self.sex_label = Label(text="เพศของตัวละคร", fg="white", bg=THEME_APP, font=('Arial', 16, 'bold'))
        self.sex_label.place(x=100, y=300)
        self.love_label = Label(text="สถานะตัวละคร", fg="white", bg=THEME_APP, font=('Arial', 16, 'bold'))
        self.love_label.place(x=100, y=400)
        # ตัวแปรรับข้อมูลที่ input() เข้ามา
        name = StringVar()
        team = StringVar()
        sex = StringVar(value="เลือกเพศ")
        love = StringVar(value="สถานะ")
        self.name_etn = Entry(width=32, textvariable=name, fg="black", bg="white", font=('Arial', 16, 'bold'))
        self.name_etn.place(x=100, y=150)
        self.team_etn = Entry(width=32, textvariable=team, fg="black", bg="white", font=('Arial', 16, 'bold'))
        self.team_etn.place(x=100, y=250)
        self.sex_combo = ttk.Combobox(width=30, font=('Arial', 16, 'bold'), textvariable=sex)
        self.sex_combo["values"] = ("ชาย", "หญิง", "อื่นๆ")
        self.sex_combo.place(x=100, y=350)
        self.love_combo = ttk.Combobox(width=30, font=('Arial', 16, 'bold'), textvariable=love)
        self.love_combo["values"] = ("โสด(กำลังตามจีบ)", "โสด(รอคนมาจีบ)", "โสด(อกหัก)", "โสด(ไม่สนใจ)", "มีคนคุยแล้ว", "มีแฟนแล้ว")
        self.love_combo.place(x=100, y=450)
        self.btn = Button(text="เข้าสู่ระบบ", fg="black", bg="white", font=('Arial', 12, 'bold'), width=30, command=self.on_click)
        self.btn.place(x=120, y=550)
        self.window.mainloop()

    def on_click(self):
        # เข้าสู่่หน้าทำข้อสอบ
        self.name = self.name_etn.get()
        self.team = self.team_etn.get()
        self.sex = self.sex_combo.get()
        self.love = self.love_combo.get()
        self.name_label.after(50, self.name_label.destroy())
        self.team_label.after(50, self.name_label.destroy())
        self.sex_label.after(50, self.sex_label.destroy())
        self.love_label.after(50, self.love_label.destroy())
        self.name_etn.after(50, self.name_etn.destroy())
        self.team_etn.after(50, self.team_etn.destroy())
        self.sex_combo.after(50, self.sex_combo.destroy())
        self.love_combo.after(50, self.love_combo.destroy())
        self.btn.after(50, self.btn.destroy())
        self.get_next_question()

    def get_next_question(self):
        # แสดงคะแนนที่ได้รับ
        self.scoreLabel = Label(text="คะแนน : 0", fg="white", bg=THEME_APP, font=('Arial', 18, 'bold'))
        self.scoreLabel.place(x=450, y=20)
        # สร้างตัวแปรเก็บข้อมูลตัวเลือก
        self.choice = choice_data
        if self.controller.hasQuestion():
            # แสดงคำถาม และตัวเลือก
            q_image, num = self.controller.nextQuestion()
            self.image = PhotoImage(file=q_image)
            Label(image=self.image).place(x=50, y=70)
            self.scoreLabel.config(text=f"คะแนน : {self.controller.score}")
            self.choice_1 = self.choice[num][0]
            self.choic_button1 = Button(text=self.choice_1, command=self.choic_pressed1, width=45, height=3, font=('Arial', 10, 'bold'))
            self.choic_button1.place(x=50, y=300)
            self.choice_2 = self.choice[num][1]
            self.choic_button2 = Button(text=self.choice_2, command=self.choic_pressed2, width=45, height=3, font=('Arial', 10, 'bold'))
            self.choic_button2.place(x=50, y=370)
            self.choice_3 = self.choice[num][2]
            self.choic_button3 = Button(text=self.choice_3, command=self.choic_pressed3, width=45, height=3, font=('Arial', 10, 'bold'))
            self.choic_button3.place(x=50, y=440)
            self.choice_4 = self.choice[num][3]
            self.choic_button4 = Button(text=self.choice_4, command=self.choic_pressed4, width=45, height=3, font=('Arial', 10, 'bold'))
            self.choic_button4.place(x=50, y=510)
            self.choice_5 = self.choice[num][4]
            self.choic_button5 = Button(text=self.choice_5, command=self.choic_pressed5, width=45, height=3, font=('Arial', 10, 'bold'))
            self.choic_button5.place(x=50, y=580)
        else:
            # เมื่อทำข้อสอบเสร็จสิ้น จะทำการส่งข้อมูล
            self.scoreLabel.config(text=f"คะแนน : {self.controller.score}")
            Label(bg=THEME_APP, width=200, height=15).place(x=50, y=70)
            Label(text="สิ้นสุดการทำข้อสอบ", fg="white", bg=THEME_APP, font=('Arial', 24, 'bold')).place(x=150, y=120)
            self.choic_button1.config(state="disabled")
            self.choic_button2.config(state="disabled")
            self.choic_button3.config(state="disabled")
            self.choic_button4.config(state="disabled")
            self.choic_button5.config(state="disabled")
            SaveData(self.name, self.team, self.sex, self.love, self.total, self.keepfalse)

    def choic_pressed1(self):
        # ส่งคำตอบ และรับค่าต่างๆเข้ามา
        ans = self.choice_1
        self.total, self.keepfalse = self.controller.checkAnswer(ans)
        self.waitNextQuestion()

    def choic_pressed2(self):
        # ส่งคำตอบ และรับค่าต่างๆเข้ามา
        ans = self.choice_2
        self.total, self.keepfalse = self.controller.checkAnswer(ans)
        self.waitNextQuestion()

    def choic_pressed3(self):
        # ส่งคำตอบ และรับค่าต่างๆเข้ามา
        ans = self.choice_3
        self.total, self.keepfalse = self.controller.checkAnswer(ans)
        self.waitNextQuestion()

    def choic_pressed4(self):
        # ส่งคำตอบ และรับค่าต่างๆเข้ามา
        ans = self.choice_4
        self.total, self.keepfalse = self.controller.checkAnswer(ans)
        self.waitNextQuestion()
    
    def choic_pressed5(self):
        # ส่งคำตอบ และรับค่าต่างๆเข้ามา
        ans = self.choice_5
        self.total, self.keepfalse = self.controller.checkAnswer(ans)
        self.waitNextQuestion()

    def waitNextQuestion(self):
        # เวลาในการตอบสนองไปหน้าต่างถัดไป
        self.window.after(100, self.get_next_question)
