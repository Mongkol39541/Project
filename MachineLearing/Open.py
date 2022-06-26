import cv2 as cv

face_model = cv.CascadeClassifier("myhaar.xml")

img = cv.imread("DOG_Poster_featurecrop.jpg")

gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = face_model.detectMultiScale(gray_scale)
    
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()