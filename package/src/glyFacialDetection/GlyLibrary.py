import cv2 as cv
from numpy import append
from . import DetectedArea
# from .DetectedArea import DetectedFace
from . import ImageManager
from . import Point
from .HelperFunctions import *
import os





def findAndDrawFacesVanilla(frame):
    """
    Create a grayscaled version of the image, find the faces, and draw them on the original image
    All using vanilla facial detection that came with opencv
    """
    package_directory = os.path.dirname(__file__)
    path = os.path.join(package_directory, "classifier\haarcascade_frontalface_default.xml")\

    print(path +" ------------------------------------------------------------")
    haar_cascasde_face = cv.CascadeClassifier(path)



    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = haar_cascasde_face.detectMultiScale(
        grayFrame, 1.1, 10, minSize=(120, 120))

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        

      

  


  