import dlib
import cv2

detector = dlib.get_frontal_face_detector()
webcam = cv2.VideoCapture(0)

while (webcam.isOpened()):
    ret, img = webcam.read()
    if ret == True:
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #dets = detector(rgb_image)
        dets, scores, subdetectors = detector.run(rgb_image, 1, 0)
    
        #for det in dets:
        #    cv2.rectangle(img, (det.left(), det.top()), (det.right(), det.bottom()), (255,0,0), 3)
        for i, det in enumerate(dets):
            cv2.rectangle(img, (det.left(), det.top()), (det.right(), det.bottom()), (255, 0,0), 3 )
            print("Detection {}, score: {}, face_type: {}".format(det, scores[i], subdetectors[i]))

        cv2.imshow("WEBCAM", img)

        if cv2.waitKey(1) == 27:
            break

webcam.release()
cv2.destroyAllWindows()