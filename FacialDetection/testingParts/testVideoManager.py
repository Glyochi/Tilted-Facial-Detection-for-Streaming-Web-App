
import sys
import cv2 as cv
sys.path.append('FacialDetection')
from VideoManager import VideoManager
from ImageManager import ImageManager
from helperFunctions import *
import time
# RUN COMMAND CAUSE INSTALLING MYSYS64 KINDA MESS WITH THE DEFAULT PYTHON.EXE USED IN COMPILATION
#  C:/'Program Files'/Python39/python.exe d:/workspace/git/Python_FacialReg/FacialDetection/testingParts/testVideoManager.py

# videoMgnr = VideoManager(30, r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testVideos\FacialDetection_TestCase.mp4')
# videoMgnr = VideoManager(60, r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testVideos\60fps_video.mp4')
# videoMgnr = VideoManager(30, 'http://192.168.1.17:8080/video')

# videoMgnr.displayStandardMethod()


videoMgnr = VideoManager(30, r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testVideos\FacialDetection_TestCase.mp4')
# videoMgnr = VideoManager(30, 'http://192.168.1.17:8080/video')
# videoMgnr.displayHowBadUnoptimizedProcessIs()
# videoMgnr.displayOptimizedMethod()
# videoMgnr.displayEvenMoreOptimizedMethod()
videoMgnr.displayStandardMethod()


# videoMgnr = VideoManager(30, r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testVideos\Gly_Speedy.mp4')
videoMgnr = VideoManager(30, r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testVideos\FacialDetection_TestCase.mp4')
# videoMgnr = VideoManager(30, "0")
# videoMgnr = VideoManager(30, 'http://192.168.1.17:8080/video')
# videoMgnr.displayHowBadUnoptimizedProcessIs()
# videoMgnr.displayOptimizedMethod()
# videoMgnr = VideoManager(30, r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testVideos\Gly_Speedy.mp4')
videoMgnr.displayEvenMoreOptimizedMethod()
# videoMgnr.correctSpeed_displayEvenMoreOptimizedMethod()q
# videoMgnr.displayStandardMethod()
# videoMgnr.displayNonInterferedMethod()



