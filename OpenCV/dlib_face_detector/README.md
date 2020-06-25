# dlib를 이용한 Face detector

**dlib**는 이미지 처리, 선형대수 등의 라이브러리 뿐만 아니라 *머신러닝 알고리즘*을 가지고 있는 C++ 툴킷이다. C++ 뿐만 아니라 python에서도 dlib 라이브러리를 사용할 수 있고, 특히 **HOG(Histogram of Oriented Gradients)** 를 이용한 얼굴 검출(face detection) 예제에서 많이 사용되고 있다.



*HOG*는 픽셀값의 변화, 즉 밝기의 변화의 방향을 나타내는 그래디언트로써 객체의 형태를 찾아낼 수 있다. 얼굴 검출 이외에도 사람의 형태를 찾아내어서 *보행자 검출*을 위해 사용할 수 있다.  **dlib.get_frontal_face_detector()** 를 사용하면 HOG를 사용한 기본 얼굴검출기를 쓸 수 있다.



- [*face_detector_from_images.py*](1.face_detector_from_images/README.md) : 정지 이미지로부터의 얼굴 탐색
- [*face_detector_from_webcam.py*](2.face_detector_from_webcam/README.md) : 웹캠 영상으로부터의 얼굴 탐색
- [*face_landmark_detection_from_image.py*](3.face_landmark_detection_from_image/README.md) : 미리 훈련된 정면 얼굴의 68개 특징점을 이용한 얼굴 탐색
- [*cnn_face_detector.py*](4.cnn_face_detector.py/README.md) : CNN을 활용한 얼굴 탐색
