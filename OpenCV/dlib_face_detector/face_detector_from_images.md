## *face_detector_from_images.py*에 대한 설명

[dlib.net](http://dlib.net/)의 얼굴 탐색을 위한 공식 예제 [face_detector.py](http://dlib.net/face_detector.py.html)를 참고한 내용입니다. dlib가 사용하는 face detector는 **HOG(Histogram of Oriented Gradients)** 특성을 *선형 분류기(linear classifier)*, *이미지 피라미드(image pyramid)*,  *슬라이딩 윈도 탐색 방식(sliding window detection scheme)*과 함께 사용합니다.

테스트할 이미지 파일을 실행파일 뒤에 차례로 나열하면 얼굴탐색을 시작합니다.  다음 분석 이미지로 넘어가려면 엔터키를 눌러줍니다.( [dlib.hit_enter_to_continue()](http://dlib.net/python/index.html#dlib.hit_enter_to_continue) ) 이번 예제에서는 처리한 영상을 보여주기 위해서 opencv 대신에 dlib의 *GUI 윈도*를 사용합니다. 사용한 함수는 다음과 같습니다.

>-  [dlib.image_window()](http://dlib.net/python/index.html#dlib.image_window) : GUI 윈도 생성
>- clear_over_lay(*self:dlib_image_window*): 이미지 윈도 위의 영상 삭제
>- set_image(*self:dlib_image_window*, *image: numpy.ndarray()*) : 이미지 윈도가 주어진 이미지를 보여준다.
>- add_overlay(*self: dlib_image_window*, *rectangles: dlib.rectangles*, *color: dlib.rgb_pixel=rgb_pixel(255,0,0)*) : 탐색한 사각형 객체를 지정된 색으로 이미지 위에 표시



예제에서 사용하는 face_detector 객체는 [dlib.get_frontal_face_detector()](http://dlib.net/python/index.html#dlib.get_frontal_face_detector)를 통해 생성합니다.  생성된 [dlib.fhog_object_detector](http://dlib.net/python/index.html#dlib.fhog_object_detector) 객체는 이미지에 대한 넘파이 배열과 좀더 정밀한 탐색을 위해 이미지를 확대하는 횟수인 *upsample_num_times* 를 입력으로 받습니다. ( 참고로 공식예제에서는 1번만 업샘플링하지만, 사용한 영상에서 2번 업샘플링했을 때 모든 얼굴을 탐색해낼 수 있었습니다.) 

객체의 __ call __ 메소드 대신에 **run()함수**를 실행할 때는 얼굴 탐색 결과와 더불어 탐색 점수(score)와 **사용된 HOG 필터**의 종류을 반환합니다. 예제에는 face_type으로 적혀있는 *sub-detector*의 내용은 [참고](https://github.com/davisking/dlib/blob/master/dlib/image_processing/frontal_face_detector.h)에서 찾을 수 있습니다. 5개의 HOG 필터는 front-looking, left-looking, right-looking,  front-looking-but-rotated-left, front-looking-but-rotated-right 입니다. 

이 필터와 계산된 점수는 인자로 설정한 threshold값까지만 구하게 되는데, 음수로 설정되면 더 많은 탐색결과를 볼 수 있고, 양수로 설정되면 더 적은 탐색결과를 갖게 됩니다. (공식예제에서는 -1로 설정되었습니다.)

