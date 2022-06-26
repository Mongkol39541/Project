import cv2
import win32com.client

class TestModel_image2:
    def detect(cap, classifier, number_of_testID, scaleFactor, minNeighbors, color, listCLF, list_nameModel):
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        listcon = []
        for (x, y, w, h) in features:
            for m in range(number_of_testID):
                id,con = listCLF[m].predict(gray[y:y+h, x:x+w])
                listcon.append(int(con))
            ar = [listcon,list_nameModel]
            con = max(listcon)
            for n in range(number_of_testID):
                if ar[0][n] == con:
                    nameModel = ar[1][n]
            if con <= 100:
                cv2.rectangle(cap, (x, y), (x+w, y+h), color, 2)
                cv2.putText(cap, nameModel, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                cv2.putText(cap, str(int(con))+"%", (x, y+20+h), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                if(cv2.waitKey(1) & 0xFF == ord('s')):
                    speaker.Speak(nameModel)
        return cap
        return cap

class TestModel_image:
    def set_testmodel(face_Model, name_of_fileimage, number_of_testID):
        face_Cascade = cv2.CascadeClassifier("data_Model/"+face_Model+".xml")
        cap = cv2.imread("test_image/"+str(name_of_fileimage)+".jpg")
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
        TestModel_image2.detect(cap, face_Cascade, number_of_testID, 1.2, 5, (0,255,0), listCLF, list_nameModel)
        cv2.imshow('frame', cap)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#face_Model = input("Face of model : ")
#name_of_fileimage = input("Name of Testimage : ")
#number_of_testID = int(input("Number of Testmodel tested : "))
#TestModel_image.set_testmodel(face_Model, name_of_fileimage, number_of_testID)