import cv2 as cv
import numpy as np
from array import *



# const
detectioncolr = (255,0,255)
detectioncolrtext = (255,255,255)
textxpos = 20

#color levels

#red
upper_R_red = 190
lower_R_red = 155
upper_G_red = 175
lower_G_red = 140
upper_B_red = 185 
lower_B_red = 150

#green
upper_R_green = 145
lower_R_green = 125
upper_G_green = 165
lower_G_green = 145
upper_B_green = 100
lower_B_green = 80

#blue
upper_R_blue = 160
lower_R_blue = 140
upper_G_blue = 210
lower_G_blue = 190
upper_B_blue = 210
lower_B_blue = 190

#yellow
upper_R_yellow = 175
lower_R_yellow = 155
upper_G_yellow = 180
lower_G_yellow = 155
upper_B_yellow = 165
lower_B_yellow = 135


cam = cv.VideoCapture(1)


cam.set(3, 640)
cam.set(4, 480)
while 1:
    rtn, img = cam.read()
    if rtn == True:
        imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        imgcopy = img.copy()

        _, thrash = cv.threshold(imgGrey, 230, 255, cv.THRESH_BINARY)
        contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        if True:
            
            count = 0
            posearr = []
    
            for contour in contours:
                cArea = cv.contourArea(contour)
                cPose = cv.moments(contour)
                if (cPose["m10"] != 0) & (cPose["m00"] != 0):
                    cx = int(cPose["m10"]/cPose["m00"])
                else:
                    cx = 0
                if (cPose["m01"] != 0) & (cPose["m00"] != 0):
                    cy = int(cPose["m01"]/cPose["m00"])
                else:
                    cy = 0
                
    
                if (cArea >400) & (cArea <100000): # filter small contours
                
                    cv.circle(imgcopy, (cx,cy),4, (0,0,0), -1)
    
                    x,y,w,h = cv.boundingRect(contour) # offsets - with this you get 'mask'
                    cv.rectangle(imgcopy,(x,y),(x+w,y+h),detectioncolr,2)
                    cv.rectangle(imgcopy,(x + textxpos -20,y - 32),(x + textxpos + 70,y),detectioncolr,-1)
                    color = np.array(cv.mean(img[y:y+h,x:x+w])).astype(np.uint8)
    
                    idx = count + 1
                    #BGR
                    print(color)
                    if (color[0] > lower_B_blue) & (color[0] < upper_B_blue) & (color[1] > lower_G_blue) & (color[1] < upper_G_blue) & (color[2] > lower_R_blue) & (color[2] < upper_R_blue):
                        cv.putText(imgcopy, "Blue", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                        c_color = "Blue"
                    elif (color[0] > lower_B_red) & (color[0] < upper_B_red) & (color[1] > lower_G_red) & (color[1] < upper_G_red) & (color[2] > lower_R_red) & (color[2] < upper_R_red):
                        cv.putText(imgcopy, "Red", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                        c_color = "Red"
                    elif (color[0] > lower_B_yellow) & (color[0] < upper_B_yellow) & (color[1] > lower_G_yellow) & (color[1] < upper_G_yellow) & (color[2] > lower_R_yellow) & (color[2] < upper_R_yellow):
                        cv.putText(imgcopy, "Yellow", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                        c_color = "Yellow"
                    elif (color[0] > lower_B_green) & (color[0] < upper_B_green) & (color[1] > lower_G_green) & (color[1] < upper_G_green) & (color[2] > lower_R_green) & (color[2] < upper_R_green):
                        cv.putText(imgcopy, "Green", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                        c_color = "Green"
                    else:
                        cv.putText(imgcopy, "Invalid", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                        #posearr.append([str(count),"Invalid", cx, cy])
                        c_color = "unknown"
                    count = count + 1
                    cv.putText(imgcopy, str(count) , (x + textxpos - 15,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
    
                    approx = cv.approxPolyDP(contour, 0.01* cv.arcLength(contour, True), True)
                    cv.drawContours(imgcopy, [approx], 0, (0, 0, 0), 1)
                    #x = approx.ravel()[0]
                    #y = approx.ravel()[1] - 5
                    if len(approx) == 4:
                        x1 ,y1, w, h = cv.boundingRect(approx)
                        aspectRatio = float(w)/h
                        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                            cv.putText(imgcopy, "Box", (x+ textxpos, y -5), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                        else:
                            cv.putText(imgcopy, "LBox", (x+ textxpos, y -5), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                        if c_color != "unknown":
                            posearr.append([str(count),c_color, cx, cy])
                    else:
                        cv.putText(imgcopy, "Invalid object", (x+ textxpos, y -5), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
    
            print(posearr)
            cv.imshow("normal img", img)
            cv.imshow("vision", imgcopy)
            cv.imshow("grey", thrash)
            cv.waitKey(2000)

cv.waitKey(1000)
cv.destroyAllWindows()  