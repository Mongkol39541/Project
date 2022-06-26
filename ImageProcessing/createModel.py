from msilib.schema import Class
import numpy as np
from PIL import Image
import os,cv2

class CreateModel:
    def train_classifier(train_Folder, crate_File):
        path = [os.path.join (train_Folder, f) for f in os.listdir(train_Folder)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert("L")
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])
            faces.append(imageNp)
            ids.append(id)
        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("data_Model/"+crate_File+".xml")

#train_Folder = str(input("Select folder of train : "))
#crate_File = str(input("Createname of Model : "))
#CreateModel.train_classifier(train_Folder, crate_File)