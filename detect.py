#This is a Face Recognition system

# Import the required libraries
import cv2
import numpy as np
import face_recognition
import os
import mysql.connector
from datetime import datetime
from datetime import date

# Initialize the list of known encodings and known names
known_images = []
imgList = []

# Grab the paths to the input images
path = 'images'
mylist = os.listdir(path)

# Loop over the image paths
for cl in mylist:
    currentimg = cv2.imread(f'{path}\\{cl}')
    known_images.append(currentimg)
    imgList.append(os.path.splitext(cl)[0])

#Define a function to find encodings of known images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodlstKnowFaces = findEncodings(known_images)
print('Encoding completed.')

cam = cv2.VideoCapture(0)
nm = "a"
while True:

    #Load the input image and convert it from BGR (OpenCV ordering) to dlib ordering (RGB)
    success, image = cam.read()
    resize_img = cv2.resize(image, (0, 0), None, 0.25, 0.25)
    resize_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)

    faceLoc = face_recognition.face_locations(resize_img)

    #Compute the facial encoding for the face
    Face_encode = face_recognition.face_encodings(resize_img, faceLoc)

    #Compare the encoding of the input image with that of known images
    for encod, faceLocation in zip(Face_encode, faceLoc):
        apt_matches = face_recognition.compare_faces(encodlstKnowFaces, encod)
        faceDistance = face_recognition.face_distance(encodlstKnowFaces, encod)

        matchesIn = np.argmin(faceDistance)

        #If matching encoding is found
        if apt_matches[matchesIn]:
            name = imgList[matchesIn].upper()
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            #Find current time
            crTime = datetime.now()
            crTime = crTime.strftime("%H:%M:%S")

            #Find current date
            crDate = date.today()
            if name != nm:

                #Connect with database
                mydb = mysql.connector.connect(host='localhost', database='records', user='root',
                                                   passwd='Hookrux@912')
                if (mydb):
                    print("Connection successfull")
                else:
                    print("failed")
                crTime = str(crTime)
                crDate = str(crDate)

                #Insert the data in the database
                var = (name, crTime, crDate)
                s = "INSERT INTO security_database VALUES (%s,%s,%s)"
                cursor = mydb.cursor()
                cursor.execute(s, var)
                mydb.commit()
                print("Record inserted successfully")
                cursor.close()
                nm = name

    cv2.imshow('Frame', image)

    #Waiting using waitkey method
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
