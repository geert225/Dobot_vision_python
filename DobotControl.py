from pickle import TRUE
from numpy import dtype
import DobotDllType as dType
import cv2 as cv
from array import *

compoort = "COM7"

x = 0
y = 0
placeCnt = 0

def setup():
    dType.SetQueuedCmdClear(api)
    dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
    dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)
    dType.SetEndEffectorSuctionCupEx(api, 0, 1)

def Loop():
    print("loop")
    #idx = camararoutine()

    idx = pickroutine(240, 0)
    waituntildone(idx)


def pickroutine(x, y):
    
    idx = dType.SetEndEffectorSuctionCupEx(api, 0, isQueued=0)
    idx = dType.SetWAITCmd(api, 1000, isQueued=1)
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x, y, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x, y, -40, 0, isQueued = 1)[0]
    idx = dType.SetEndEffectorSuctionCupEx(api, 1, isQueued=0)
    idx = dType.SetWAITCmd(api, 1000, isQueued=1)
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x, y, 20, 0, isQueued = 1)[0]
    #idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    return idx

def camararoutine():
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    idx = dType.SetWAITCmd(api, 1000, isQueued=1)
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    return [idx, x, y]

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
dType.DisconnectDobot(api)


