import dlib
import cv2

detector = dlib.get_frontal_face_detector()
webcam = cv2.VideoCapture(0)

while True:
    ret, img = webcam.read()
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(rgb_image)
    
    for det in dets:
        cv2.rectangle(img, (det.left(), det.top()), (det.right(), det.bottom), (255,0,0), 3)
    cv2.imshow("WEBCAM", img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyWindows()