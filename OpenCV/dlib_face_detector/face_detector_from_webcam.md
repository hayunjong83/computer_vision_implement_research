# face_detector_from_webcam.py에 대한 설명

*face_detector_from_images.py* 에서 나아가 정지영상이 아닌 실시간 웹캠 입력에서 얼굴을 분석해보는 예제다. 

웹캠에서 영상을 입력받고 출력하기 위해서 OpenCV를 사용하였다. 웹캠으로부터 라이브 스트림을 받는 것은 **OpenCV-Python Tutorials** 의 [Getting Started with Videos](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html) 를 참고하면 좋다. 우선, *VideoCapture* 객체를 만든다. cv2.VideoCapture()의 인자는 디바이스 인덱스로서 0은 디폴트 카메라를 가리킨다. 카메라가 제대로 동작하지 않으면 isOpened()가 False이거나, read()의 첫번째 리턴값이 False이므로 둘 중 하나만 확인하면 된다.

기타 다른 부분은 정지영상 때와 동일하다. 다만 OpenCV는 기본적으로 색상공간(color space)를 RGB가 아닌 **BGR** 을 사용한다.( [참고](https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/) ) 영상 위에 (255, 0, 0)으로 그려주는 사각형의 색깔이 파란색인 것을 볼 수 있다. 반면, dlib는 기본적으로 rgb 이미지를 넘파이 배열로 받아들여 분석한다.( *dlib.load_rgb_image()* ) 따라서 cv.cvtColor() 함수에 cv2.COLOR_BGR2RGB 플래그를 사용해 색공간을 바꿔준다. 

