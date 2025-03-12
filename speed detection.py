import cv2
import numpy as np
from timeit import default_timer as timer

tanTheta = 80 / 180
# print(tanTheta)
# dn = float(input("Enter the perpendicular distance from camera: "))
dn = 180
dp = 2 * dn * tanTheta

motion = 0
prevMotion = 0
speed = 0.0
vid = cv2.VideoCapture(0)
check, firstFrame = vid.read()
if not check or firstFrame is None:
    print("Error: Could not access webcam")
    exit()
firstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
while True:
    check, color = vid.read()
    if motion == 0:
        prevMotion = 0
    else:
        prevMotion = 1
    motion = 0
    frame = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
    diffFrame = cv2.absdiff(firstFrame, frame)
    threshFrame = cv2.threshold(diffFrame, 30, 255, cv2.THRESH_BINARY)[1]
    threshFrame = cv2.dilate(threshFrame, np.ones((3, 3), np.uint8), iterations=2)
    threshFrame = cv2.erode(threshFrame, np.ones((3, 3), np.uint8), iterations=2)
    (cnts, _) = cv2.findContours(threshFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 3000:
            continue
        motion = 1
        if prevMotion == 0 and motion == 1:
            tStart = timer()
        (x, y, w, h) = cv2.boundingRect(contour)
        color = cv2.rectangle(color, (x, y), (x + w, y + h), (0, 255, 0), 3)
    if prevMotion == 1 and motion == 0:
        tEnd = timer()
        time = tEnd - tStart
        speed = round((dp / time) * (9.0 / 25.0), 2)

    cv2.putText(color, "speed : " + str(speed) + "km/hr", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('window', color)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
