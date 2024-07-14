import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while True:

    ret,img = cap.read()
    if ret == True:
        cv2.imshow("capture",img)

        key = cv2.waitKey(30) & 0xff

        if key == 27:
            break

        if key == ord(' '):
            cv2.imwrite('mycapture.jpg',img)
        
        cap.release()

        cv2.destroyAllWindows()
    else:
        print("카메라를 찾을수 없음")
        break
