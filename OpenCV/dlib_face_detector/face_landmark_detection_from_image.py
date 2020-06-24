import sys
import os
import dlib

if len(sys.argv)!= 3:
    print(
        """
        Usage in Windows: 
            python face_landmark_detection_from_image.py   [trained shape predictor model name]    [filename]

        ex) python face_landmark_detection_from_image.py   shape_predictor_68_face_landmarks.dat   lovelys.jpg
        """
    )

# divide landmarks
jaw = list(range(0, 17))
r_eyebrow = list(range(17, 22))
l_eyebrow = list(range(22, 27))
nose = list(range(27, 36))
r_eye = list(range(36, 42))
l_eye = list(range(42, 48))
out_mouth = list(range(48, 61))
in_mouth = list(range(61, 68))

landmarks = [jaw, r_eyebrow, l_eyebrow, nose, r_eye, l_eye, out_mouth, in_mouth]

# set color (RGB type)
colors = [(100,0,0), (255,0,0),(255,127,0),(255, 255,0), (0, 255,0), (0, 0, 255),(75, 0, 130), (143, 0, 255)]

predictor_path = sys.argv[1]
image_file = sys.argv[2]

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
win = dlib.image_window()

print("Processing file: {}".format(image_file))
img = dlib.load_rgb_image(image_file)

win.clear_overlay()
win.set_image(img)

dets = detector(img, 2)
print("Number of faces detected: {}".format(len(dets)))
for index, det in enumerate(dets):
    print("Detection {}: LEFT: {}, TOP: {}, RIGHT: {}, BOTTOM: {}".format(index, det.left(), det.top(), det.right(), det.bottom()))
    shape = predictor(img, det)
    
    # when you want to visualize divided landmarks 
    for marks, color  in zip(landmarks , colors ):
        for i in marks:
            win.add_overlay_circle(shape.part(i), 1, dlib.rgb_pixel(color[2], color[1], color[0]))
    
    # when you jush want to see whole landmarks
    # win.add_overlay(shape)


win.add_overlay(dets)
dlib.hit_enter_to_continue()

