import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
imageDir = os.path.join(BASE_DIR, "Images")

#print(f'Base Directory: {BASE_DIR}')
#print(f'Image Directory: {imageDir}')

y_labels = []
x_train = []
labelIdsDir = {}
currentId = 0

cascade_file_name = "haarcascade_frontalface_alt_tree.xml"
face_cascade = cv2.CascadeClassifier(cascade_file_name)

recogniser = cv2.face.LBPHFaceRecognizer_create()

for root, dirs, files in os.walk(imageDir):
    #print(f'root: {root}')
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg") or \
                file.endswith("PNG") or file.endswith("JPG") or file.endswith("JPEG"):
            imageFilePath = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").capitalize()

            if not label in labelIdsDir:
                labelIdsDir[label] = currentId
                currentId += 1
            id_ = labelIdsDir[label]

            #print(id_)
            #print(imageFilePath)

            pilImage = Image.open(imageFilePath).convert("L").resize((550, 550), Image.ANTIALIAS) #Open and Convert into Gray Scale
            imageArray = np.array(pilImage, "uint8")

            faces = face_cascade.detectMultiScale(imageArray, scaleFactor=1.5, minNeighbors=5)
            #print(faces)

            for (x, y, w, h) in faces:
                imageRoi = imageArray[y:y+h, x:x+w]
                x_train.append(imageRoi)
                y_labels.append(id_)

with open("label.pickle", "wb") as f:
    pickle.dump(labelIdsDir, f)

recogniser.train(x_train, np.array(y_labels))
recogniser.save("trainer.yml")

#print(x_train)
#print(y_labels)
#print(labelIdsDir)


