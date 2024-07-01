import cv2
from cv2 import destroyAllWindows
import numpy as np

img = cv2.imread("laneline.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2, y2), (0, 255, 0), 3)
#print(lines)

#cv2.HoughLines()
#cv2.HoughLinesP()
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
