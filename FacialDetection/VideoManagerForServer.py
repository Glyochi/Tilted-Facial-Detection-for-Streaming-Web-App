import cv2 as cv
from numpy import append
from DetectedArea import DetectedArea, DetectedFace
from ImageManager import ImageManager
from Point import Point
from helperFunctions import *
import time
import threading
import queue


class VideoManagerForServer:
    """
    A manager that stores multiple frames (images) and manage how to display them and perform facial detection on those frames.
    """

    HARDCODED_pairOfEyesDistanceRange = (1.5, 3.5)
    HARDCODED_distanceVariation_EyeToCorners_MinOfMax = 0.8
    HARDCODED_updateFaceLocationSearchMultiplier = 1.4
    HARDCODED_similarSizeScale = 0.5
    HARDCODED_faceNotFoundCountLimit = 3

    def __init__(self, videoFps=0):
        """
        Construct a VideoManager object
            :param videoFps: the fps of the input video
            :param dir: the directory to the video
        """
        self.videoFps = videoFps
        self.faces = []

    def processNextFrame(self, frame):
        """
        SHOW THE NORMAL JUST GRAB NEWFRAME WHENEVER IT COMES INSTEAD OF LIMITING FRAMERATE THING
        """
        haar_cascasde_face = cv.CascadeClassifier(
            "classifier/haarcascade_frontalface_default.xml")

        # frameTimeInterval = 1/self.videoFps
        # if frame is read correctly/ new frame is available, then ret is True.

        
        # Our operations on the frame come here
        frame = resizeMinTo500(frame)

        # startTime = time.time()
        grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # print(f"grayscale runtime {time.time() - startTime:0.6f} seconds")

        # startTime = time.time()
        faces = haar_cascasde_face.detectMultiScale(
            grayFrame, 2, 6, minSize=(30, 30))
        # print(f"Haarcascade Runtime {time.time() - startTime:0.6f} seconds")

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        

      

  


  