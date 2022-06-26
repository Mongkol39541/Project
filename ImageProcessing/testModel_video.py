import cv2
import win32com.client

class TestModel_video4:
    def draw_boundary(img, classifier, number_of_testID, scaleFactor, minNeighbors, color, clf, list_nameModel):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        listcon = []
        for (x, y, w, h) in features:
            for m in range(number_of_testID):
                id,con = clf[m].predict(gray[y:y+h, x:x+w])
                listcon.append(int(con))
            ar = [listcon,list_nameModel]
            con = max(listcon)
            for n in range(number_of_testID):
                if ar[0][n] == con:
                    nameModel = ar[1][n]
            if con <= 100:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                cv2.putText(img, nameModel, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                cv2.putText(img, str(int(con))+"%", (x, y+20+h), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                if(cv2.waitKey(1) & 0xFF == ord('s')):
                    speaker.Speak(nameModel)
        return img

class TestModel_video3:
    def detect(img, face_Cascade, number_of_testID, clf, list_nameModel):
        img = TestModel_video4.draw_boundary(img, face_Cascade, number_of_testID, 1.2, 5, (0,255,0), clf, list_nameModel)
        return img

class TestModel_video2:
    def red_clf(cap, face_Cascade, listCLF, number_of_testID, list_nameModel):
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frame = TestModel_video3.detect(frame, face_Cascade, number_of_testID, listCLF, list_nameModel)
                cv2.imshow('frame', frame)
                if(cv2.waitKey(1) & 0xFF == ord('q')):
                    break
            else:
                break
        return cap

class TestModel_video:
    def set_testmodel(face_Model, name_of_filevideo, number_of_testID):
        face_Cascade = cv2.CascadeClassifier("data_Model/"+face_Model+".xml")
        cap = cv2.VideoCapture("test_video/"+str(name_of_filevideo)+".mp4")
        listID = []
        listCLF = []
        list_nameModel = []
        for i in range(number_of_testID):
            readFile = str(input("ModelFile : "))
            name_model = str(input("Name of Model : "))
            listID.append(readFile)
            list_nameModel.append(name_model)
        for j in range(number_of_testID):
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("data_Model/"+listID[j]+".xml")
            listCLF.append(clf)
        TestModel_video2.red_clf(cap, face_Cascade, listCLF, number_of_testID, list_nameModel)
        cap.release()
        cv2.destroyAllWindows()

#face_Model = input("Face of model : ")
#name_of_filevideo = input("Name of Testvideo : ")
#number_of_testID = int(input("Number of Testmodel tested : "))
#TestModel_video.set_testmodel(face_Model, name_of_filevideo, number_of_testID)