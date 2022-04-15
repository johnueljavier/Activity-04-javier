import cv2
import os

while True:
    pc = input("Your file[insert '.jpg' at the end]:")
    flag = input("\nPress[1] for colored image \n press[0] for grayscale image:")
    if os.path.exists(pc) and flag == '0':
        imge= cv2.imread(pc, 0)
        cv2.imshow(pc,imge)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break
    elif os.path.exists(pc) and flag == '1':
        imge= cv2.imread(pc, 1)
        cv2.imshow(pc,imge)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break

    else:
        print("denied")

	
