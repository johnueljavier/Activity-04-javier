import cv2
import os

while True:
	pc = input("Your file[insert '.jpg' at the end]:")

	if os.path.exists(pc):
		imge= cv2.imread(pc, 1)
		cv2.imshow(pc,imge)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break

	else:
		print("denied")