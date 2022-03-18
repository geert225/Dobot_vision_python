import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

api = dType.load()
state = dType.ConnectDobot(api, "", 115200)[0]


if (state == dType.DobotConnect.DobotConnect_NoError):
    
    
    
    dType.SetQueuedCmdClear(api)
    
    
    #patameters 
    dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

    
    

    
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    dType.SetWAITCmd(api, 1000, isQueued=0)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, 60, 20, 0, isQueued = 1)[0]
    lastidx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240, -60, 20, 0, isQueued = 1)[0]
    
    while lastidx > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)


dType.DisconnectDobot(api)
