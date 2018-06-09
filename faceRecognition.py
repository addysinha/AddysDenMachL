import cv2
import numpy as np
import os
import pickle

cascade_file_name = "haarcascade_frontalface_alt_tree.xml"
face_cascade = cv2.CascadeClassifier(cascade_file_name)

recogniser = cv2.face.LBPHFaceRecognizer_create()
recogniser.read("trainer.yml")

videoCapture = cv2.VideoCapture(0)

labels={}
with open("label.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k, v in og_labels.items()}

while(True):
    ret, frame = videoCapture.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    faces = face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.5, minNeighbors=5, minSize=(4,4))
    for (x,y,w,h) in faces:
        imageRoi = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)[y:y+h, x:x+w]
        id_, conf = recogniser.predict(imageRoi)
        if conf >= 80:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 4)
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 0)
            thickness = 2
            cv2.putText(frame, name, (x,y), font, 1, color, thickness, cv2.LINE_AA)

    cv2.imshow("Frame", frame)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()

