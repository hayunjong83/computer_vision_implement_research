import sys
import dlib

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()

if len(sys.argv) == 1:
    print("""
    Usage in Windows: 
    python face_detector.py [filename1, [filename2] ...)
    """)
else:
    for file in sys.argv[1:]:
        print("Processing file: {}".format(file))
        img = dlib.load_rgb_image(file)

        # set number of upsampling according to your test image
        dets = detector(img, 2)
        print("    - Number of faces detected: {}".format(len(dets)))
        for index, det in enumerate(dets):
            print("        - Detection: {}: LEFT: {}, TOP: {}, RIGHT: {}, BOTTOM: {}".format(
                index, det.left(), det.top(), det.right(), det.bottom()))
    
        win.clear_overlay()
        win.set_image(img)
        win.add_overlay(dets)
        dlib.hit_enter_to_continue()

if len(sys.argv) > 1:
    for file in sys.argv[1:]:
        img = dlib.load_rgb_image(file)
        print("Print score of file: {}".format(file))
        dets , scores, subdetectors = detector.run(img, 2, 0)
        for i, det in enumerate(dets):
            print("Detection {}, score: {}, face_type: {}".format(
                det, scores[i], subdetectors[i]
            ))


