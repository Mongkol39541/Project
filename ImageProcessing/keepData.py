import cv2

class KeepData_2:
    def create_dataset(img, id, img_id, keep_folder):
        cv2.imwrite(str(keep_folder)+"/pic."+str(id)+"."+str(int(img_id/10))+".jpg", img)
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
        coords = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            coords = [x, y, w, h]
        return img, coords
    def detect(img, face_Cascade, img_id, che_id, keep_folder, id):
        img, coords = KeepData_2.draw_boundary(img, face_Cascade, 1.2, 5, (0,0,255), "Face")
        if img_id == che_id:
            che_id += 10
            if len(coords) == 4 :
                result = img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
                KeepData_2.create_dataset(result, id, img_id, keep_folder)
        return img, che_id

class KeepData:
    def set_keepdata(faceModel, number_of_trainID, keep_folder):
        face_Cascade = cv2.CascadeClassifier("data_Model/"+faceModel+".xml")
        listFile = []
        for j in range(number_of_trainID):
            nameFile = input("Train video at {0} : ".format(j+1))
            listFile.append(nameFile)
        for i in range(number_of_trainID):
            id = i+1
            cap = cv2.VideoCapture("train_video/"+str(listFile[i])+".mp4")
            img_id = 0
            che_id = 0
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    frame, che_id = KeepData_2.detect(frame, face_Cascade, img_id, che_id, keep_folder, id)
                    cv2.imshow(str(keep_folder), frame)
                    img_id += 1
                    if(cv2.waitKey(1) & 0xFF == ord('q')):
                        break
                else:
                    break
        cap.release()
        cv2.destroyAllWindows()

#face_Model = input("Face of model : ")
#number_of_trainID = int(input("Number of videos trained : "))
#keep_folder = input("Name of keepfolder : ")
#KeepData.set_keepdata(face_Model, number_of_trainID, keep_folder)