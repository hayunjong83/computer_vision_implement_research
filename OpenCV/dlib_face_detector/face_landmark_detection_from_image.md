## *face_landmark_detection_from_image.py* 에 대한 설명

dlib의 default detector의 사용에서 나아가, 얼굴에서 파악할 수 있는 **특징점(landmark)** 를  통한 얼굴 탐색에 관한 내용이다. 여기에서 사용하는 **shape_predictor_68_face_landmarks.dat** 파일은 300-W 데이터셋에서 훈련되어 추출된 68개의 얼굴 특징점(facial landmark) 정보를 가지고 있다.

<img src="facial_landmark.png" alt="68 facial landmark" style="zoom:67%;" />



> ICCV(International Conference on Computer Vision) 2013에는 사람의 얼굴 위치를 찾아내는 첫번째 대회인 **300 Faces in-the-Wild Challenge** 가 개최되었다. 여기에 사용된 데이터셋이 [*300-W dataset*](https://ibug.doc.ic.ac.uk/resources/300-W/)으로 *i · bug (intelligent behaviour understanding group)* 에서 관리되고 있다. 
>
> 위의 그림이 300-W 데이터셋에서 훈련된 사람 얼굴 **전면**의 68개 특징점이다. 세부사항은 [Facial Point Annotations](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/) 를 참고한다. 여기에서 사용한 미리 훈련된 특징점 정보는 [dlib.net/files/](http://dlib.net/files/) 에서 받을 수 있다. 
>
> 단, 유의할 점은 데이터셋과 훈련된 특징점 파일은 연구목적으로만 사용가능하고 상업적 사용이 불가능하다. 상업적 사용을 위해서는 iBUG 300-W 데이터셋의 라이센스를 갖고 있는 영국의 Imperial College London에 문의할 필요가 있다.

[**dlib.shape_predictor()**](http://dlib.net/python/index.html#dlib.shape_predictor) 을 통해 파일로부터 shape_predictor를 로드하면, 이전에 다른 데이터셋에서 dlib.train_shape_predictor()를 통해 훈련한 모델을 불러올 수 있다. shape_predictor()를 사용하면 영상에서 탐색하려는 객체의 위치를 표현하는 [**dlib.full_object_detection**](http://dlib.net/python/index.html#dlib.full_object_detection) 가 반환된다. 좀 더 구체적으로말하면 위의 68개 특징점마다의 중심점(자료형: dlib.point)을 **full_object_detection.part(인덱스)** 로 접근할 수 있게 된다. 위 그림에 따라 인덱스를 분류하면 다음과 같다.

- 턱선(jawline) : 0번 ~ 16번
- 오른쪽 눈썹(right_eyebrow) : 17번 ~ 21번
- 왼쪽 눈썹(left_eyebrow) : 22번 ~ 26번
- 코(nose) : 27번 ~ 35번
- 오른쪽 눈(right_eye) : 36번 ~ 41번
- 왼쪽 눈(left_eye) :  42번 ~ 47번
- 입술 윤곽(mouth_outline) : 48번 ~ 60번
- 입술 안쪽(mouth_inner) : 61번 ~ 67번

앞서 *face_detector_from_images.py* 에서는 기본 탐색자가 찾은 사각형을 그리기 위해 *add_overlay()* 를 사용하였다. 4개의 점 정보를 가진 dlib.rectangle과 달리 중심점 하나의 x, y 좌표를 가진 dlib.point 즉, full_object_detection.part(i)를 넘겨주면 오류가 발생한다. 그러나 **full_object_detection 객체를 직접 add_overlay()** 에 넘겨주면 내부적으로 처리해서 중심점들을 모두 이미지 위에 표현해준다. 단, 사각형을 그릴 때 기본적으로 지정된 색이 *빨간색* 인 반면, 중심점들은 기본지정색이 *파란색* 인 점이 다르다.

하지만, dlib에서 중심점을 바로 그려주는 메소드를 가지고 있다. **add_overlay_circle()** 에 중심점 좌표와, 반지름을 지정해주면 각각의 특징점을 원으로 표현이 가능하다. OpenCV를 통해서 특징점을 따로 그리거나, 전체 특징점을 분리하지 않고 그리는 예제는 흔하기 때문에, *add_overlay_circle()* 을 이용해 부분별로 다른 색상으로 표현해보았다. 
