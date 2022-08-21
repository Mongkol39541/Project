# รันโปรแกรม
from question import Question
from data import question_data
from controller import Controller
from ui import UserInterface

all_question = []
for item in question_data:
    # เปลี่ยนข้อมูลจากรูป Dict เป็น List
    image = item["image"]
    answer = item["answer"]
    question = Question(image, answer)
    all_question.append(question)
# ส่งค่าที่ได้ไปทำงาน
controller = Controller(all_question)
UserInterface(controller)
