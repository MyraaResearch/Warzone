import os
import cv2
import numpy as n
from PIL import Image
reco=cv2.createEigenFaceRecognizer()
detec=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
path='dataset'

def getImage(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    Ids=[]
    for imagepath in imagePaths:
        pilImage=Image.open(imagepath).convert('L');
        imageNp=n.array(pilImage,'uint8')
        Id=int(os.path.split(imagepath)[-1].split(".")[1])
        faces=detec.detectMultiScale(imageNp)
        for (x,y,w,h) in faces: 
            Ids.append(Id)
            faceSamples.append(imageNp[y:y+h,x:x+w])
            cv2.imshow("trainning",imageNp);
            cv2.waitKey(10)
    return Ids,faceSamples
Ids,faceScamples=getImage(path)
reco.train(faces,n.array(Ids))
reco.save("trainner/trainning.yml");
cv2.destroyAllWindows()
