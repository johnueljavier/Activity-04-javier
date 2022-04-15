import cv2
filepath ="ayaka.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("awel",image)
cv2.waitKey(0)
cv2.destroyAllWindows()