# Selective search

**object detection** 알고리즘은 이미지에 존재하는 객체의 판별과 동시에 그 위치를 알려준다. 
객체의 위치를 특정하기 위해서는, 우선 이미지의 패치(patch, 또는 부분 영역 sub-region)를 선택해야 한다. 가장 직관적인 패치 생성 방식은 **슬라이딩 윈도(sliding window)**다. 하지만 슬라이딩 윈도는 연산 비용이 너무 많이 든다.

> 슬라이딩 윈도를 사용한 object detection의 단점
>
> 1.  이미지의 모든 영역을 탐색해야 한다.
> 2. 각기 다른 스케일의 패치에 대한 탐색이 필요하다.
>    따라서 고정비율 이미지가 아닌 경우, 연산 비용이 매우 크다.

**Selective search** 방식은 객체가 존재할 가능성이 큰 위치를 먼저 찾아내는 **region proposal** 알고리즘에서 초기에 사용되던 방식이다. 우선, **그래프 기반 분할(Graph-based Segmentation)**으로부터 다양한 크기와 비율의 초기 후보 영역을 생성한다.  그 다음, 이 후보영역을 (색상/텍스처/크기/모양) 4가지 기준의 **유사도(similarity)**로부터 반복적으로 통합해 나간다. 

> Selective search의 계층적(hierarchical) 세그먼테이션
>
> 1. 그래프 기반 분할 방식으로부터 과다분할(over-segmentation)된 후보 영역을 찾는다.
> 2. 바운딩 박스(bounding box)가 추가된 후보 영역을 유사도 기준을 이용하여 묶어 나간다. 가장 큰 단일 영역이 될 때까지, 이 과정을 반복한다.
>
> 작은 세그먼트에서부터 점차 큰 세그먼트를 형성하는 bottom-up 방식이다.

Selective search 방식은 **높은 재현율(high recall)**을 가지므로, 생성된 제안 영역 중에는 탐색 중인 객체가 포함되었을 확률이 높다.

OpenCV에는 Selective Search를 수행하는 **SelectiveSearchSegmentation** 클래스가 구현되어 있다. 이 클래스에는 재현율(recall)과 연산 속도의 트레이드 오프를 고려한 두 가지 방식이 있다.

1. fast / low recall
   switchToSelectiveSearchFast()
2. slow / high recall
   switchToSelectiveSearchQuality()

[Selective Search for Object Detection](C++/Python) 을 참고하여 작성된 프로그램에서, 빠른 속도의 구현에서는 357개의 후보영역이, 높은 재현율의 구현에서는 1209개의 후보영역이 각각 제안되었다. 좀 더 구체적인 내용은 논문 [Selective Search for Object Recognition](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)을 참고하는 것이 좋다.

![f_mode](.\image\f_mode.png)

![q_mode](.\image\q_mode.png)

