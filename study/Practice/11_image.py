import cv2

img_file = "file/img_1.png"

img = cv2.imread(img_file)  # 이미지 읽기기

if img is not None:
    img_resize = cv2.resize(img,(960, 540)) #사이즈 변경
    cv2.imshow("IMG",img_resize)
    cv2.waitKey()
    cv2.destroyAllWindows()

else:
    print("image file not found")

