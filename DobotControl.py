from pickle import TRUE
from numpy import dtype
import DobotDllType as dType
import cv2 as cv
from array import *

compoort = "COM6"

def setup():
    dType.SetQueuedCmdClear(api)
    dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

def Loop():
    print("loop")
    idx = camararoutine()

    idx = pickroutine(x, y)
    waituntildone(idx)


def pickroutine():
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    idx = dType.SetWAITCmd(api, 1000, isQueued=1)
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    return idx

def camararoutine():
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    idx = dType.SetWAITCmd(api, 1000, isQueued=1)
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    return idx

def placeroutine():
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    idx = dType.SetWAITCmd(api, 1000, isQueued=1)
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    return idx

def waituntildone(idx):
    while idx > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)














CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

api = dType.load()
state = dType.ConnectDobot(api, compoort, 115200)[0]


if (state == dType.DobotConnect.DobotConnect_NoError):
    
    
    
    
    
    setup()
    while TRUE:
        Loop()
    
    #patameters 
    


    
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    dType.SetWAITCmd(api, 1000, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    lastidx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    
    while lastidx > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)


dType.DisconnectDobot(api)


