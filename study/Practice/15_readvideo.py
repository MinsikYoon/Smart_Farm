import cv2

cap = cv2.VideoCapture('RECORD.mp4')

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    f_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    f_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    f_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    delay = int(1000/cap.get(cv2.CAP_PROP_FPS))

    print('Frames/sec : ',fps,'FPS')
    print('Frame count: ',f_count)
    print('Frame width : ',f_width)
    print('Frame height : ', f_height)
    print('delay : ',delay)

while True:
    ret,frame = cap.read()
    if ret :
        cv2.imshow('My_video',frame)
        if cv2.waitKey(delay)&0xFF == 27:
            print("ESC Key Pressed")
            break
    else:
        print(ret,frame)
        break
cap.release()
cv2.destroyAllWindows()