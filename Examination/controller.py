class Controller:
    def __init__(self, data):
        # รับค่าเข้ามา
        self.question_list = data
        self.question_number = 0
        self.score = 0
        self.current = None
        self.keepfalse = []

    # ไปยังข้อถัดไป
    def nextQuestion(self):
        self.current = self.question_list[self.question_number]
        self.question_number += 1
        return f"{self.current.image}", self.question_number - 1

    # หยุดทำงานเมื่อทำครบทุกข้อ
    def hasQuestion(self):
        return self.question_number < len(self.question_list)

    # ตรวจสอบคำตอบ
    def checkAnswer(self, userInput):
        currect_answer = self.current.answer
        if userInput.lower() == currect_answer.lower():
            # ได้รับคะแนน
            self.score += 1
            return self.score, self.keepfalse
        else:
            # เก็บข้อมูลข้อสอบที่ทำผิด
            self.keepfalse.append(self.question_number)
            return self.score, self.keepfalse
