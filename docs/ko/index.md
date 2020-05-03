---
layout: default
title: 딥러닝
author: Alfredo Canziani
lang-ref: home
lang: ko
translation-date: 22 Mar 2020
translator: Gio
---

**DS-GA 1008 · 2020 봄 · [NYU CENTER FOR DATA SCIENCE](http://cds.nyu.edu/)**

| 강사 | 얀 르쿤 & 알프래도 캔지아니 |
| 이론    | 월요일 16:55 – 18:35, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| 실습    | 화요일 19:10 – 20:00, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| [PIAZZA](https://piazza.com/nyu/spring2020/dsga1008/home)      | Access code: `DLSP20` |
| 강의자료    | [Google Drive](https://bitly.com/DLSP20), [Notebooks](https://github.com/Atcold/pytorch-Deep-Learning) |


## 소개
이 코스에서는 지도 학습과 비지도 학습, 임베딩 기법, 메트릭 학습, 합성곱 및 순환 신경망 등의 최신 딥러닝 및 표현 학습 기법과 컴퓨터 비전, 자연어 이해, 음성 인식 분야에서 이들의 적용 사례들을 소개합니다. 이 수업을 듣기 위해선 [DS-GA 1001 Intro to Data Science](https://cds.nyu.edu/academics/ms-curriculum/) 강의나 학부 수준의 머신 러닝 지식이 필요합니다.

## 수업

**범례**: 🖥 슬라이드, 📓 주피터 노트북, 🎥 유튜브 영상.

<table>
<!-- =============================== HEADER ================================ -->
  <thead>
    <tr>
      <th>주차</th>
      <th align="left">포맷</th>
      <th align="left">제목</th>
      <th align="left">자료</th>
    </tr>
  </thead>
  <tbody>
<!-- =============================== WEEK 1 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ko/week01/01">①</a></td>
      <td rowspan="2">이론</td>
      <td><a href="{{site.baseurl}}/ko/week01/01-1">딥러닝의 등장과 역사</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ko/week01/01-2">딥러닝의 발전</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="{{site.baseurl}}/ko/week01/01-3">신경망 (NN)</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ko/week02/02">②</a></td>
      <td rowspan="2">이론</td>
      <td><a href="{{site.baseurl}}/ko/week02/02-1">확률적 경사 하강법과 역전파</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
        <a href="https://www.youtube.com/watch?v=d9vdh3b787Y">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ko/week02/02-2">경사 하강법의 실제 적용</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="{{site.baseurl}}/ko/week02/02-3">신경망의 학습</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=WAn6lip5oWk">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ko/week03/03">③</a></td>
      <td rowspan="2">이론</td>
      <td><a href="{{site.baseurl}}/ko/week03/03-1">파라미터 변환</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
        <a href="https://youtu.be/FW5gFiJb-ig">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ko/week03/03-2">합성곱 신경망</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="{{site.baseurl}}/ko/week03/03-3">자연 신호의 성질</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
        <a href="https://youtu.be/kwPWpVverkw">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="{{site.baseurl}}/ko/week04/04">④</a></td>
      <td rowspan="1">실습</td>
      <td><a href="{{site.baseurl}}/ko/week04/04-1">1D 합성곱</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
        <a href="https://youtu.be/OrBEon3VlQg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ko/week05/05">⑤</a></td>
      <td rowspan="2">이론</td>
      <td><a href="{{site.baseurl}}/ko/week05/05-1">최적화 I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
        <a href="https://youtu.be/--NZb480zlg">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ko/week05/05-2">최적화 II</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="{{site.baseurl}}/ko/week05/05-3">CNN, autograd</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/03-autograd_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/extra/b-custom_grads.ipynb">📓</a>
        <a href="https://youtu.be/eEzCZnOFU1w">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 6 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ko/week06/06">⑥</a></td>
      <td rowspan="2">이론</td>
      <td><a href="{{site.baseurl}}/ko/week06/06-1"></a>-</td>
      <td rowspan="2">
        <a href=""></a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ko/week06/06-2"></a>-</td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="{{site.baseurl}}/ko/week06/06-3"></a>-</td>
      <td>
      </td>
    </tr>
<!-- =============================== WEEK 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ko/week07/07"></a>⑦</td>
      <td rowspan="2">이론</td>
      <td><a href="{{site.baseurl}}/ko/week07/07-1"></a>-</td>
      <td rowspan="2">
        <a href=""></a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ko/week07/07-2"></a>준지도 학습, 에너지 기반 모델</td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="{{site.baseurl}}/ko/week07/07-3">오토인코더</a></td>
      <td>
        <a href="https://drive.google.com/file/d/1FEleglSDblyrSpHdGhaDydEQI36Rq5uB/">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/10-autoencoder.ipynb">📓</a>
      </td>
    </tr>
  </tbody>
</table>


<!--
## People

| 역할 | 사진 | 연락처 | 약력 |
|:-----|:-----:|:--------|:------|
|교수|<img src="./images/Yann.png" width="100" height="100">|<a href="https://twitter.com/ylecun">Yann LeCuna</a><br>yann@cs.nyu.edu|Silver Professor in CS at NYU<br>and Turing Award winner|
|교수|<img src="https://avatars1.githubusercontent.com/u/2119355" width="100" height="100">|<a href="https://twitter.com/alfcnz">Alfredo Canziani</a><br>canziani@nyu.edu|Asst. Prof. in CS at NYU|
|조교수|<img src="https://pbs.twimg.com/profile_images/1186879808845860864/czRv3g1G_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/marikgoldstein">Mark Goldstein</a><br>goldstein@nyu.edu|PhD student in CS at NYU|
|웹 관리자|<img src="https://pbs.twimg.com/profile_images/673997980370927616/vMXf545j_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/ebetica">Zeming Lin</a><br>zl2799@nyu.edu|PhD student in CS at NYU|
|채점자|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Serkan Karakulak <br>sk7685@nyu.edu|
|채점자|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Raghav Jajodia <br>rj1408@nyu.edu|
|채점자|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Priyank Pathak <br>pp1953@nyu.edu|
|채점자|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Chiao-Hsun Wang <br>chw371@nyu.edu|
|채점자|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Pedro Vidal<br>pmh314@nyu.edu|
|채점자|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Bixing Yan <br>by783@nyu.edu|
-->
