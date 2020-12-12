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

| 강사    | 얀 르쿤 & 알프래도 캔지아니 |
| 이론    | 월요일 16:55 – 18:35, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| 실습    | 화요일 19:10 – 20:00, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| 포럼    | [r/NYU_DeepLearning](https://www.reddit.com/r/NYU_DeepLearning/) |
| 강의자료| [Google Drive](https://bitly.com/DLSP20), [Notebooks](https://github.com/Atcold/pytorch-Deep-Learning) |


## 소개
이 코스에서는 지도 학습과 비지도 학습, 임베딩 기법, 메트릭 학습, 합성곱 및 순환 신경망 등의 최신 딥러닝 및 표현 학습 기법과 컴퓨터 비전, 자연어 이해, 음성 인식 분야에서 이들의 적용 사례들을 소개합니다. 이 수업을 듣기 위해선 [DS-GA 1001 Intro to Data Science](https://cds.nyu.edu/academics/ms-curriculum/) 강의나 학부 수준의 머신 러닝 지식이 필요합니다.

## 강의

**범례**: 🖥 슬라이드, 📓 주피터 노트북, 🎥 유튜브.

<table>
<!-- =============================== HEADER ================================ -->
  <thead>
    <tr>
      <th>주차</th>
      <th align="left">형식</th>
      <th align="left">제목</th>
      <th align="left">자료</th>
    </tr>
  </thead>
  <tbody>
<!-- =============================== WEEK 1 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week01/01">①</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week01/01-1">딥러닝의 등장과 역사</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2">딥러닝의 발전</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week01/01-3">신경망 (NN)</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">②</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week02/02-1">확률적 경사 하강법과 역전파</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
        <a href="https://www.youtube.com/watch?v=d9vdh3b787Y">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week02/02-2">경사하강법의 적용</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week02/02-3">신경망의 학습</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=WAn6lip5oWk">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week03/03">③</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week03/03-1">매개변수 변환</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
        <a href="https://youtu.be/FW5gFiJb-ig">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week03/03-2">합성곱 신경망</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week03/03-3">자연 신호의 성질</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
        <a href="https://youtu.be/kwPWpVverkw">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="week04/04">④</a></td>
      <td rowspan="1">실습</td>
      <td><a href="week04/04-1">1D 합성곱</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
        <a href="https://youtu.be/OrBEon3VlQg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week05/05">⑤</a></td>
      <td rowspan="2">실습</td>
      <td><a href="week05/05-1">최적화 I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
        <a href="https://youtu.be/--NZb480zlg">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week05/05-2">최적화 II</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week05/05-3">CNN, autograd</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/03-autograd_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/extra/b-custom_grads.ipynb">📓</a>
        <a href="https://youtu.be/eEzCZnOFU1w">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 6 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week06/06">⑥</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week06/06-1">CNN의 적용</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1opT7lV0IRYJegtZjuHsKhlsM5L7GpGL1">🖥️</a>
        <a href="https://drive.google.com/open?id=1sdeVBC3nuh5Zkm2sqzdScEicRvLc_v-F">🖥️</a>
        <a href="https://youtu.be/ycbMGyCPzvE">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week06/06-2">순환 신경망과 어텐션</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week06/06-3">RNN의 학습</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/08-seq_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/09-echo_data.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/04%20-%20RNN.pdf">🖥️</a>
        <a href="https://youtu.be/8cAffg2jaT0">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week07/07">⑦</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week07/07-1">에너지 기반 모델</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1z8Dz1YtkOEJpU-gh5RIjORs3GGqkYJQa">🖥️</a>
        <a href="https://youtu.be/tVwV14YkbYs">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week07/07-2">SSL, EBM</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week07/07-3">오토인코더</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/10-autoencoder.ipynb">📓</a>
        <a href="https://youtu.be/bggWQ14DD9M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 8 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week08/08">⑧</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week08/08-1">대조적 방법</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Zo_PyBEO6aNt0GV74kj8MQL7kfHdIHYO">🖥️</a>
        <a href="https://youtu.be/ZaVP2SY23nc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week08/08-2">정규화 잠재 변수<sup>Regularised latent</sup></a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week08/08-3">VAE의 학습</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/11-VAE.ipynb">📓</a>
        <a href="https://youtu.be/7Rb4s9wNOmc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 9 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week09/09">⑨</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week09/09-1">희소성<sup>Sparsity</sup></a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1wJRzhjSqlrSqEpX4Omagb_gdIkQ5f-6K">🖥️</a>
        <a href="https://youtu.be/Pgct8PKV7iw">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week09/09-2">세계 모델과 생산적 적대 신경망</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week09/09-3">GAN의 학습</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/pytorch/examples/tree/master/dcgan">📓</a>
        <a href="https://youtu.be/xYc11zyZ26M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 10 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="week10/10">⑩</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week10/10-1">CV SSL I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=16lsnDN2HIBTcRucbVKY5B_U16c0tNQhR">🖥️</a>
        <a href="https://youtu.be/0KeR6i1_56g">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week10/10-2">CV SSL II</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week10/10-3">Predictive Control</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/09%20-%20Controller%20learning.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/14-truck_backer-upper.ipynb">📓</a>
        <a href="https://youtu.be/A3klBqEWR-I">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 11 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="week11/11">⑪</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week11/11-1">활성화 함수</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1AzFVLG7D4NK6ugh60f0cJQGYF5OL2sUB">🖥️</a>
        <a href="https://drive.google.com/file/d/1rkiZy0vjZqE2w7baVWvxwfAGae0Eh1Wm">🖥️</a>
        <a href="https://drive.google.com/file/d/1tryOlVAFmazLLZusD2-UfReFMkPk5hPk">🖥️</a>
        <a href="https://youtu.be/bj1fh3BvqSU">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week11/11-2">손실 함수</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week11/11-3">PPUU</a></td>
      <td>
        <a href="http://bit.ly/PPUU-slides">🖥️</a>
        <a href="http://bit.ly/PPUU-code">📓</a>
        <a href="https://youtu.be/VcrCr-KNBHc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 12 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="week12/12">⑫</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week12/12-1">NLP를 위한 딥러닝 I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/149m3wRavTp4DQZ6RJTej8KP8gv4jnkPW/">🖥️</a>
        <a href="https://youtu.be/6D4EWKJgNn0">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week12/12-2">NLP를 위한 딥러닝 II</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week12/12-3">어텐션 & 트렌스포머</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/10%20-%20Attention%20%26%20transformer.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/15-transformer.ipynb">📓</a>
        <a href="https://youtu.be/f01J0Dri-6k">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 13 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="week13/13">⑬</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week13/13-1">그래프 합성곱 신경망 I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1oq-nZE2bEiQjqBlmk5_N_rFC8LQY0jQr/">🖥️</a>
        <a href="https://youtu.be/Iiv9R6BjxHM">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week13/13-2">그래프 합성곱 신경망 II</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week13/13-3">그래프 합성곱 신경망 III</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/11%20-%20GCN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/16-gated_GCN.ipynb">📓</a>
        <a href="https://youtu.be/2aKXWqkbpWg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 14 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="week14/14">⑭</a></td>
      <td rowspan="2">이론</td>
      <td><a href="week14/14-1">구조화된 예측</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1qBu-2hYWaGYEXeX7kAU8O4S2RZ1hMjsk/">🖥️</a>
        <a href="https://youtu.be/gYayCG6YyO8">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week14/14-2">그래프 기반 방법</a></td></tr>
    <tr>
      <td rowspan="1">실습</td>
      <td><a href="week14/14-3">과적합과 정규화</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/07%20-%20Regularisation.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/12-regularization.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/08%20-%20Bayesian%20NN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/13-bayesian_nn.ipynb">📓</a>
        <a href="https://youtu.be/DL7iew823c0">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 15 =============================== -->
    <tr>
      <td rowspan="2" align="center"><a href="week15/15">⑮</a></td>
      <td rowspan="2">실습</td>
      <td><a href="week15/15-1">Latent-Variable EBM의 추론</a></td>
      <td rowspan="1">
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf">🖥️</a>
        <a href="https://youtu.be/sbhr2wjU1-I">🎥</a>
      </td>
    </tr>
    <tr>
      <td><a href="week15/15-2">Latent-Variable EBM의 학습</a></td>
      <td rowspan="1">
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf">🖥️</a>
        <a href="https://youtu.be/XLSb1Cs1Jao">🎥</a>
      </td>
    </tr>
  </tbody>
</table>


## 강의자

| 직책 | 사진 | 연락처 | 소개 |
|:-----|:-----:|:--------|:------|
|교수|<img src="https://github.com/Atcold/pytorch-Deep-Learning/raw/master/docs/images/Yann.png" width="100" height="100">|<a href="https://twitter.com/ylecun">Yann LeCun</a><br>yann@cs.nyu.edu|Silver Professor in CS at NYU<br>and Turing Award winner|
|교수|<img src="https://avatars1.githubusercontent.com/u/2119355" width="100" height="100">|<a href="https://twitter.com/alfcnz">Alfredo Canziani</a><br>canziani@nyu.edu|Asst. Prof. in CS at NYU|
|조교|<img src="https://pbs.twimg.com/profile_images/1186879808845860864/czRv3g1G_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/marikgoldstein">Mark Goldstein</a><br>goldstein@nyu.edu|PhD student in CS at NYU|
|웹 관리자|<img src="https://pbs.twimg.com/profile_images/673997980370927616/vMXf545j_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/ebetica">Zeming Lin</a><br>zl2799@nyu.edu|PhD student in CS at NYU|


<!--
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Serkan Karakulak <br>sk7685@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Raghav Jajodia <br>rj1408@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Priyank Pathak <br>pp1953@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Chiao-Hsun Wang <br>chw371@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Pedro Vidal<br>pmh314@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Bixing Yan <br>by783@nyu.edu|
-->


## Disclaimer

<!-- All other texts found on this site are lecture notes taken by students of the New York University during lectures given by Yann Le Cun, Alfredo Canziani, Ishan Misra, Mike Lewis and Xavier Bresson.
Thus the texts in English were written by about 130 people, which has an impact on the homogeneity of the texts (some write in the past tense, others in the present tense; the abbreviations used are not always the same; some write short sentences, while others write sentences of up to 5 or 6 lines, etc.).
It is possible that there may be some omissions: typing errors, spelling mistakes, etc. If you notice any, we invite you to submit a PR on the [GitHub directory of the site](https://github.com/Atcold/pytorch-Deep-Learning/pulls) specifying with an `[EN]` that it concerns the English translation.

Wishing you a deep reading !-->

이 사이트의 목차를 제외한 모든 텍스트는 Yann Le Cun, Alfredo Canziani, Ishan Misra, Mike Lewis와 Xavier Bresson가 뉴욕대학교에서 진행한 수업을 기반으로 뉴욕대학교 학생들이 작성한 강의 노트입니다.
즉, 본 사이트의 글은 130명 이상의 서로 다른 사람이 영어로 작성하고 이를 다시 20여 명의 사람이 번역한 바, 글의 용어나 시제 등이 통일되어 있지 않을 수 있습니다.
또한, 오탈자나 내용상의 모순 등 다양한 오류가 있을 수 있습니다. 이러한 오류를 발견하신다면, [본 사이트의 깃허브](https://github.com/Atcold/pytorch-Deep-Learning/pulls)에 PR을 남겨주세요. (`[KR]` 태그를 제목에 붙여, 사이트의 한글 자료와 관련된 것임을 알려주세요!)

즐거운 딥러닝 learning 되시길 바랍니다!
