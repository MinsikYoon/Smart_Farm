import cv2

cap = cv2.VideoCapture(0)


if cap.isOpened():
    delay = int(1000/cap.get(cv2.CAP_PROP_FPS))
    while True:
        ret,img = cap.read()
        if ret:
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Camera",img_gray)
            if cv2.waitKey(delay) & 0xFF == 27:
                print("ESC Key Pressed")
                break
        else:
            print(ret,img)
            break
else:
    print("camera not opened")

cap.release()
cv2.destroyAllWindows()

