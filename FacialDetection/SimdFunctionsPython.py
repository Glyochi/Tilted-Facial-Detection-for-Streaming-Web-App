from ctypes import *
import ctypes.util
import cv2 as cv
import ctypes

simd = ctypes.cdll.LoadLibrary(r"D:\workspace\git\Python_FacialReg\libraries\simd\bin\v142\x64\Release\Simd.dll")

img = cv.imread(r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testImages\people_half_flipped.jpg')
# detection = simd.Detection()
detector = simd.SimdDetection.Detection()