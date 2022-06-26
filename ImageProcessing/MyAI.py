from keepData import KeepData
from createModel import CreateModel
from testModel_video import TestModel_video
from testModel_image import TestModel_image
from testModel_capture import TestModel_capture

# data collection process
start_keepData = str(input("Start-keepData(yes/no) : ")) # รับคำสั่ง yes/no
if start_keepData == "yes": # ทำงานเมื่อคำสั่งเป็น yes
    face_Model = input("Face of model : ")  # รับ model เข้าไปทำงาน
    number_of_trainID = int(input("Number of videos trained : "))   # จำนวนวีดีโอที่ต้องการ train จากโฟเดอร์ train_video
    keep_folder = input("Name of keepfolder : ")    # ต้องการเก็บข้อมูลโฟเดอร์อะไร
    KeepData.set_keepdata(face_Model, number_of_trainID, keep_folder) # ส่งค่า face_Model, number_of_trainID, keep_folder เข้าไปทำงานในฟังก์ชั่น
else :
    pass

# Modeling process
start_createModel = str(input("Start-createModel(yes/no) : "))  # รับคำสั่ง yes/no
if start_createModel == "yes":  # ทำงานเมื่อคำสั่งเป็น yes
    train_Folder = str(input("Select folder of train : "))  # เลือกโฟเดอร์ที่ต้องการทดสอบ
    crate_File = str(input("Createname of Testmodel : "))   # ตั้งชื่อ Testmodel
    CreateModel.train_classifier(train_Folder, crate_File)  # ส่งค่า train_Folder, crate_File เข้าไปทำงานในฟังก์ชั่น
else :
    pass

# Model testing procedures
start_testModel = str(input("Start-testModel(video/image/capture) : ")) # รับคำสั่ง video/image/capture
if start_testModel == "video":  # ทำงานเมื่อคำสั่งเป็น video
    face_Model = input("Face of model : ")  # รับ model เข้าไปทำงาน
    name_of_filevideo = input("Name of Testvideo : ")   # ชื่อของวีดีโอที่ต้องการ test จากโฟเดอร์ test_video
    number_of_testID = int(input("Number of Testmodel tested : "))  # จำนวน Testmodel ที่ต้องการ test
    TestModel_video.set_testmodel(face_Model, name_of_filevideo, number_of_testID)
if start_testModel == "image":  # ทำงานเมื่อคำสั่งเป็น image
    face_Model = input("Face of model : ")  # รับ model เข้าไปทำงาน
    name_of_fileimage = input("Name of Testimage : ")   # ชื่อของวีดีโอที่ต้องการ test จากโฟเดอร์ test_image
    number_of_testID = int(input("Number of Testmodel tested : "))  # จำนวน Testmodel ที่ต้องการ test
    TestModel_image.set_testmodel(face_Model, name_of_fileimage, number_of_testID)
if start_testModel == "capture":    # ทำงานเมื่อคำสั่งเป็น capture
    face_Model = input("Face of model : ")  # รับ model เข้าไปทำงาน
    number_of_testID = int(input("Number of Testmodel tested : "))  # จำนวน Testmodel ที่ต้องการ test
    TestModel_capture.set_testmodel(face_Model, number_of_testID)
else :
    pass