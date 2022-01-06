from threading import Thread, Lock
from .FrameThread import FrameThread
import time

class ServerVideoManager:
    def __init__(self, frameRate, socket):
        # Used for the emitting thread
        self.playing = True
        self.frameRate = frameRate

        self.frameThreads = [None, None, None, None, None]
        self.freeThreadIDs = [0, 1, 2, 3, 4]
        self.returnedFrameID = 0
        self.receivedFrameID = 0
        
        self.socket = socket

        self.emittingThread = None
        self.frameLock = Lock()


    def start(self):
        self.playing = True
        self.emittingThread = Thread(target=emitter, args=[self])
        self.emittingThread.start()
        
    def stop(self):
        self.playing = False



    def processNextFrame(self, customFunction, frame, endPoint):
        # Its pretty impossible to have all 5 threads taken up
        if not len(self.freeThreadIDs):
            print('*****************************************************************************************')
            print('*  ERROR: in VideoManager file: No more free threads. Sir can I have sum more threads?  *')
            print('*****************************************************************************************')
            return

        threadID = self.freeThreadIDs.pop(0)

        self.frameThreads[threadID] = FrameThread(threadID, self.receivedFrameID, customFunction, frame, self.frameLock, endPoint)
        self.frameThreads[threadID].start()
        
        self.receivedFrameID += 1
    
    



def emitter(videoManager):
    
    while videoManager.playing: 
        # print("DEBUG FREE THREADS COUNT    " , len(videoManager.freeThreadIDs))
        if len(videoManager.freeThreadIDs) < 5:
            

            i = 0
            frameThreads = videoManager.frameThreads
            freeThreadIDs = videoManager.freeThreadIDs
            finishedThreadIDs = []


            videoManager.frameLock.acquire()
            
            while i < len(frameThreads):
                

                # If thread t has finished running
                # if not frameThreads[i].is_alive():
                
                if frameThreads[i] != None and not frameThreads[i].is_alive():
                    # add the finished thread id onto the freeThreadIDs attribute of the videoManager
                    freeThreadIDs.append(i)

                    # add the finished thread id onto the finishedThreadArray thats gonna be used later
                    finishedThreadIDs.append(i)

                i += 1            

            videoManager.frameLock.release()
            

            if len(finishedThreadIDs) >= 1:
                # If more than one thread finished, then only send the latest one's output to the client
                
                latestFrameIDIndex = 0
                latestFrameID = frameThreads[finishedThreadIDs[latestFrameIDIndex]].frameID
                

                # Finding the newest frame that just got rendered by frameThread
                i = 1
                while i < len(finishedThreadIDs):

                    if(frameThreads[finishedThreadIDs[i]].frameID > latestFrameID):
                        latestFrameIDIndex = i
                        latestFrameID = frameThreads[finishedThreadIDs[i]].frameID

                    i += 1

                # if the latest frame that just got rendered by frameThread is newer than the last frame that we sent back to the client
                # then send that latest frame to the client
                if latestFrameID > videoManager.returnedFrameID:
                    temp = frameThreads[finishedThreadIDs[latestFrameIDIndex]]
                    videoManager.returnedFrameID = latestFrameID
                    videoManager.socket.emit(temp.endPoint, temp.frame)

                # if the latest frame is behind the last frame that was sent to the client, then do nothing
                


                # Removing the finished threads out of the running threads array
                for i in finishedThreadIDs:
                    frameThreads[i] = None

            time.sleep(1/(3*videoManager.frameRate))
        else:
            time.sleep(1/(6 * videoManager.frameRate))
                



