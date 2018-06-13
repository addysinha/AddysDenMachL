import cv2
import numpy as np
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "..\\Images\\")

CASCADE_FILE = "..\\haarcascade_frontalface_alt_tree.xml"
CASCADE_HANDLER = cv2.CascadeClassifier(CASCADE_FILE)

x_train = []
y_label = []
labelDir = {}
labelId = 0

recogniserAlgo = cv2.face.LBPHFaceRecognizer_create()

for root, dir, files in os.walk(IMAGE_DIR):
    #print(f'root: {root}')
    #print(f'dir: {dir}')
    #print(f'files: {files}')

    for file in files:
        if file.endswith("JPG") or file.endswith("JPEG") or file.endswith("PNG") \
                or file.endswith("jpg") or file.endswith("jpeg") or file.endswith("png"):

            label = os.path.basename(root).replace(" ", "-").capitalize()
            #print(f'Label: {label}')

            if not label in labelDir:
                labelDir[label] = labelId
                labelId += 1

            #id_ = list(labelDir.keys())[list(labelDir.values()).index(label)]
            id_ = labelDir[label]
            print(label, labelId, id_)

            imageFileWithPath = os.path.join(root, file)

            rgbImage = cv2.resize(cv2.imread(imageFileWithPath, 1), (0,0), fx=0.5, fy=0.5)
            grayImage = cv2.cvtColor(rgbImage, cv2.COLOR_RGB2GRAY)
            faces = CASCADE_HANDLER.detectMultiScale(grayImage, scaleFactor=1.25, minNeighbors=5)

            for (x, y, w, h) in faces:
                faceROI = grayImage[y:y+h, x:x+w]
                #print(file, x, y, w, h)
                #cv2.imshow(file, faceROI)
                x_train.append(faceROI)
                y_label.append(id_)

with open("label.pickle", "wb") as f:
    pickle.dump(labelDir, f)

recogniserAlgo.train(x_train, np.array(y_label))
recogniserAlgo.save("trainer.yml")

#print(y_label)
#print(x_train)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

