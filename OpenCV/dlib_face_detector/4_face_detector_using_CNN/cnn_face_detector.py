import sys
import dlib

if len(sys.argv)!= 3:
    print(
        """
        Usage in Windows: 
            python face_landmark_detection_from_image.py   [pretrained cnn detect model name]    [filename]
        """
    )
    exit()

cnn_face_detector = dlib.cnn_face_detection_model_v1(sys.argv[1])
win = dlib.image_window()

img = dlib.load_rgb_image(sys.argv[2])
dets = cnn_face_detector(img, 1)
rects = dlib.rectangles()

print("Numbers of faces detected: {}".format(len(dets)))
for index, det in enumerate(dets):
    r = det.rect    
    print("Detection {}: LEFT: {}, TOP: {}, RIGHT: {}, BOTTOM: {} : Confidence: {}".format(index, r.left(), r.top(), r.right(), r.bottom(), det.confidence ))
    rects.append(r)

win.clear_overlay()
win.set_image(img)
win.add_overlay(rects)
dlib.hit_enter_to_continue()


