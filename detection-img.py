import cv2 as cv
import numpy as np
from array import *

def getvision():
    img = cv.imread(imgpath)
    imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgcopy = img.copy()

    _, thrash = cv.threshold(imgGrey, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    count = 0
    posearr = []

    for contour in contours:
        cArea = cv.contourArea(contour)
        cPose = cv.moments(contour)

        cx = int(cPose["m10"]/cPose["m00"])
        cy = int(cPose["m01"]/cPose["m00"])

        if (cArea >400) & (cArea <100000): # filter small contours

            cv.circle(imgcopy, (cx,cy),4, (0,0,0), -1)

            x,y,w,h = cv.boundingRect(contour) # offsets - with this you get 'mask'
            cv.rectangle(imgcopy,(x,y),(x+w,y+h),detectioncolr,2)
            cv.rectangle(imgcopy,(x + textxpos -20,y - 32),(x + textxpos + 70,y),detectioncolr,-1)
            color = np.array(cv.mean(img[y:y+h,x:x+w])).astype(np.uint8)

            idx = count + 1
            print(color)
            if (color[0] > 225) & (color[0] < 255) & (color[2] < 200):
                cv.putText(imgcopy, "Blue", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                posearr.append([str(count),"blue", cx, cy])
            elif (color[0] > 230) & (color[0] < 255) & (color[2] > 200):
                cv.putText(imgcopy, "Purple", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                posearr.append([str(count),"Purple", cx, cy])
            elif (color[0] < 230) & (color[2] > 200) & (color[1] < 200):
                cv.putText(imgcopy, "Red", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                posearr.append([str(count),"Red", cx, cy])
            elif (color[0] < 230) & (color[2] > 200) & (color[1] > 200):
                cv.putText(imgcopy, "Yellow", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                posearr.append([str(count),"Yellow", cx, cy])
            elif (color[1] > 200) & (color[2] < 200) & (color[0] < 200):
                cv.putText(imgcopy, "Green", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                posearr.append([str(count),"Green", cx, cy])
            else:
                cv.putText(imgcopy, "Invalid", (x + textxpos,y - 20), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)
                posearr.append([str(count),"Invalid", cx, cy])
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
            else:
                cv.putText(imgcopy, "Invalid object", (x+ textxpos, y -5), cv.FONT_HERSHEY_COMPLEX, 0.5, detectioncolrtext)

    
    cv.imshow("normal img", img)
    cv.imshow("vision", imgcopy)
    cv.imshow("grey", thrash)
    cv.waitKey(6000)







# const
detectioncolr = (255,0,255)
detectioncolrtext = (255,255,255)
textxpos = 20
imglist = ['img/test.jpg','img/test2.jpg','img/test3.jpg','img/test4.jpg','img/test5.jpg','img/test6.jpg','img/test7.jpg','img/test8.jpg','img/test9.jpg']

#images
for imgpath in imglist:
    getvision()
    



cv.waitKey(1000)
cv.destroyAllWindows()  



