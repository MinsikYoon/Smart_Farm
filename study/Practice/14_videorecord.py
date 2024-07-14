import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('RECORD.mp4',fourcc,20.0,(640,480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame',frame)
        out.write(frame)

    else:
        print('no frame')
        break


    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows() 