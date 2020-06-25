## *cnn_face_detector.py*에 대한 설명

*HOG* 를 사용했던 지난 dlib 라이브러리 예제에서 나아가, CNN 모델을 사용하는 얼굴 탐색에 대한 예제다. 딥러닝 예제이긴 하지만, dlib에서 제공하는 사전 훈련모델을 라이브러리처럼 사용하고 딥러닝 프레임워크를 사용하지 않았기 때문에 **OpenCV** 폴더에서 실행하였다. 

공식 예제에서 사용하는 pre-trained 모델은 *mmoc_human_face_detector.dat*를 사용한다. 

> dlib.net의 Davis E. King이 제안한 **Max-Margin Object Detection**에 관한 [논문](https://arxiv.org/abs/1502.00046)을 참조한다. 이 예제는 특성 추출을 HOG특성 대신 CNN을 이용해 수행하는 것으로서 , [Easily Create High Quality Object Detectors with Deep Learning](http://blog.dlib.net/2016/10/easily-create-high-quality-object.html) 를 참고하면 이해하기 쉽다.



얼굴 탐색 모델을 로드하기 위해서 [**dlib.cnn_face_detection_model_v1**](http://dlib.net/python/index.html#dlib.cnn_face_detection_model_v1) 클래스를 사용한다.  다양한 모델 파일을 받아서 사용할 수 있다. *cnn_face_detection_model_v1* 객체는 [**mmod_rectangles**](http://dlib.net/python/index.html#dlib.mmod_rectangle) 객체를 반환한다.  *mmod_rectangle*의 리스트와 더불어 각각에 대한 *신뢰 점수(confidence score)*를 가지고 있다. 