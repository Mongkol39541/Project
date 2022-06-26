import cv2 
import os

path = os.getcwd()
path = path +'/test_image'
file = os.listdir(path)
for name in file :
    print(name)
    image = cv2.imread(path+'/'+name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier('myhaar.xml')
    rects = detector.detectMultiScale(gray, scaleFactor=1.05,
                                      minNeighbors=2, minSize=(40,40))

    if rects != ():
        for (i, (x, y, w, h)) in enumerate(rects):
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, "Here is Taki ", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    else :  cv2.putText(image, "Where is Taki kun", (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    
    cv2.imshow("Taki detector", image)
    if cv2.waitKey() == 32 : # press spacebar to step to next picture
        cv2.imwrite('{}'.format(name)+'.png',image)
        continue 
    else : break