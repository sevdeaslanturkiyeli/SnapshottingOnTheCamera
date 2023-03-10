import cv2
import time
cpt = 0
maxFrames = 30 #number of photos requested

cap=cv2.VideoCapture(0)

while cpt < maxFrames:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    cv2.imshow("Frame", frame) # show image in window
    #Here, you should write the file's path where photos are to be saved.
    cv2.imwrite("C:.../images/photograph_%d.jpg" %cpt, frame)
    time.sleep(0.5)
    cpt += 1
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()