---
layout: default
title: 深層学習
author: Alfredo Canziani
lang-ref: home
lang: ja
translation-date: 12 Aug 2020
translator: Go Inoue
---

**DS-GA 1008 · 2020年度春学期 · [ニューヨーク大学データ・サイエンス・センター](http://cds.nyu.edu/)**

| 講師 | Yann LeCun & Alfredo Canziani |
| 講義    | 月曜日 16:55 – 18:35, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| 演習    | 火曜日 19:10 – 20:00, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| FORUM       | [r/NYU_DeepLearning](https://www.reddit.com/r/NYU_DeepLearning/) |
| 資料    | [Google Drive](https://bitly.com/DLSP20), [Notebooks](https://github.com/Atcold/pytorch-Deep-Learning) |


## 概要

この講義では、深層学習や表現学習の最新技術について、主に教師あり・教師なし深層学習、埋め込み手法、距離学習、畳み込み・再帰型ニューラルネットワークや、それらを用いたコンピュータビジョン、自然言語処理、音声認識などの応用技術を取り扱います。
この講義は「[DS-GA 1001 Intro to Data Science](https://cds.nyu.edu/academics/ms-curriculum/)」あるいは大学院レベルの機械学習科目をすでに履修していることを前提とします。

<!-- This course concerns the latest techniques in deep learning and representation learning, focusing on supervised and unsupervised deep learning, embedding methods, metric learning, convolutional and recurrent nets, with applications to computer vision, natural language understanding, and speech recognition. The prerequisites include: [DS-GA 1001 Intro to Data Science](https://cds.nyu.edu/academics/ms-curriculum/) or a graduate-level machine learning course. -->

## 講義

**凡例**: 🖥 スライド, 📓 Jupyter notebook, 🎥 YouTubeビデオ.

<table>
<!-- =============================== HEADER ================================ -->
  <thead>
    <tr>
      <th>週</th>
      <th align="left">形式</th>
      <th align="left">タイトル</th>
      <th align="left">資料</th>
    </tr>
  </thead>
  <tbody>
<!-- =============================== WEEK 1 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week01/01">①</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week01/01-1">歴史とモチベーション</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week01/01-2">発展と深層学習</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week01/01-3">ニューラルネット(NN)</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week02/02">②</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week02/02-1">SGDと誤差逆伝播法</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
        <a href="https://www.youtube.com/watch?v=d9vdh3b787Y">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week02/02-2">実用的な誤差逆伝播法</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week02/02-3">NNの訓練</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=WAn6lip5oWk">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week03/03">③</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week03/03-1">パラメータ変換</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
        <a href="https://youtu.be/FW5gFiJb-ig">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week03/03-2">CNN</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week03/03-3">自然界の信号の特性</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
        <a href="https://youtu.be/kwPWpVverkw">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="{{site.baseurl}}/ja/week04/04">④</a></td>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week04/04-1">1D畳み込み</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
        <a href="https://youtu.be/OrBEon3VlQg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week05/05">⑤</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week05/05-1">最適化手法I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
        <a href="https://youtu.be/--NZb480zlg">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week05/05-2">最適化手法II</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week05/05-3">CNN、自動微分</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/03-autograd_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/extra/b-custom_grads.ipynb">📓</a>
        <a href="https://youtu.be/eEzCZnOFU1w">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 6 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week06/06">⑥</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week06/06-1">CNNの応用技術</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1opT7lV0IRYJegtZjuHsKhlsM5L7GpGL1">🖥️</a>
        <a href="https://drive.google.com/open?id=1sdeVBC3nuh5Zkm2sqzdScEicRvLc_v-F">🖥️</a>
        <a href="https://youtu.be/ycbMGyCPzvE">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week06/06-2">RNNと注意機構</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week06/06-3">RNNの訓練</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/04%20-%20RNN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/08-seq_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/09-echo_data.ipynb">📓</a>
        <a href="https://youtu.be/8cAffg2jaT0">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week07/07">⑦</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week07/07-1">エネルギーベースモデル(EBM)</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1z8Dz1YtkOEJpU-gh5RIjORs3GGqkYJQa">🖥️</a>
        <a href="https://youtu.be/tVwV14YkbYs">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week07/07-2">自己教師あり学習(SSL)、EBM</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week07/07-3">自己符号化器</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/10-autoencoder.ipynb">📓</a>
        <a href="https://youtu.be/bggWQ14DD9M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 8 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week08/08">⑧</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week08/08-1">対照学習法</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Zo_PyBEO6aNt0GV74kj8MQL7kfHdIHYO">🖥️</a>
        <a href="https://youtu.be/ZaVP2SY23nc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week08/08-2">正則化された潜在変数をもつEBM</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week08/08-3">変分自己符号化器(VAE)の訓練</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/11-VAE.ipynb">📓</a>
        <a href="https://youtu.be/7Rb4s9wNOmc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 9 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week09/09">⑨</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week09/09-1">スパース性</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1wJRzhjSqlrSqEpX4Omagb_gdIkQ5f-6K">🖥️</a>
        <a href="https://youtu.be/Pgct8PKV7iw">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week09/09-2">世界モデル、GAN</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week09/09-3">GANの訓練</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/pytorch/examples/tree/master/dcgan">📓</a>
        <a href="https://youtu.be/xYc11zyZ26M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 10 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week10/10">⑩</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week10/10-1">コンピュータビジョンにおける自己教師あり学習I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=16lsnDN2HIBTcRucbVKY5B_U16c0tNQhR">🖥️</a>
        <a href="https://youtu.be/0KeR6i1_56g">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week10/10-2">コンピュータビジョンにおける自己教師あり学習II</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week10/10-3">予測制御</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/09%20-%20Controller%20learning.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/14-truck_backer-upper.ipynb">📓</a>
        <a href="https://youtu.be/A3klBqEWR-I">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 11 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week11/11">⑪</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week11/11-1">活性化関数</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1AzFVLG7D4NK6ugh60f0cJQGYF5OL2sUB">🖥️</a>
        <a href="https://drive.google.com/file/d/1rkiZy0vjZqE2w7baVWvxwfAGae0Eh1Wm">🖥️</a>
        <a href="https://drive.google.com/file/d/1tryOlVAFmazLLZusD2-UfReFMkPk5hPk">🖥️</a>
        <a href="https://youtu.be/bj1fh3BvqSU">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week11/11-2">ロス関数</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week11/11-3">不確実な状況下における制御と計画</a></td>
      <td>
        <a href="http://bit.ly/PPUU-slides">🖥️</a>
        <a href="http://bit.ly/PPUU-code">📓</a>
        <a href="https://youtu.be/VcrCr-KNBHc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 12 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/ja/week12/12">⑫</a></td>
      <td rowspan="2">講義</td>
      <td><a href="{{site.baseurl}}/ja/week12/12-1">自然言語処理のための深層学習I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/149m3wRavTp4DQZ6RJTej8KP8gv4jnkPW/">🖥️</a>
        <a href="https://youtu.be/6D4EWKJgNn0">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/ja/week12/12-2">自然言語処理のための深層学習II</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="{{site.baseurl}}/ja/week12/12-3">注意機構 & トランスフォーマ</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/10%20-%20Attention%20%26%20transformer.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/15-transformer.ipynb">📓</a>
        <a href="https://youtu.be/f01J0Dri-6k">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 13 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week13/13">⑬</a></td>
      <td rowspan="2">講義</td>
      <td><a href="en/week13/13-1">グラフ畳み込みネットワーク I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1oq-nZE2bEiQjqBlmk5_N_rFC8LQY0jQr/">🖥️</a>
        <a href="https://youtu.be/Iiv9R6BjxHM">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week13/13-2">グラフ畳み込みネットワーク II</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="en/week13/13-3">グラフ畳み込みネットワーク III</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/11%20-%20GCN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/16-gated_GCN.ipynb">📓</a>
        <a href="https://youtu.be/2aKXWqkbpWg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 14 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week14/14">⑭</a></td>
      <td rowspan="2">講義</td>
      <td><a href="en/week14/14-1">構造化予測</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1qBu-2hYWaGYEXeX7kAU8O4S2RZ1hMjsk/">🖥️</a>
        <a href="https://youtu.be/gYayCG6YyO8">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week14/14-2">グラフ手法</a></td></tr>
    <tr>
      <td rowspan="1">演習</td>
      <td><a href="en/week14/14-3">正則化とベイズ</a></td>
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
      <td rowspan="2" align="center"><a href="en/week15/15">⑮</a></td>
      <td rowspan="2">演習</td>
      <td><a href="en/week15/15-1">潜在変数EBMの推論</a></td>
      <td rowspan="1">
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf">🖥️</a>
        <a href="https://youtu.be/sbhr2wjU1-I">🎥</a>
      </td>
    </tr>
    <tr>
      <td><a href="en/week15/15-2">潜在変数EBMの学習</a></td>
      <td rowspan="1">
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf">🖥️</a>
        <a href="https://youtu.be/XLSb1Cs1Jao">🎥</a>
      </td>
    </tr>
  </tbody>
</table>


## 担当者

| 役割 | 写真 | 連絡先 | 所属 |
|:-----|:-----:|:--------|:------|
|講師|<img src="../images/Yann.png" width="100" height="100">|<a href="https://twitter.com/ylecun">Yann LeCun</a><br>yann@cs.nyu.edu|ニューヨーク大学コンピュータ・サイエンス学科シルバー教授<br>チューリング賞受賞者|
|講師|<img src="https://avatars1.githubusercontent.com/u/2119355" width="100" height="100">|<a href="https://twitter.com/alfcnz">Alfredo Canziani</a><br>canziani@nyu.edu|ニューヨーク大学コンピュータ・サイエンス学科助教|
|アシスタント|<img src="https://pbs.twimg.com/profile_images/1186879808845860864/czRv3g1G_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/marikgoldstein">Mark Goldstein</a><br>goldstein@nyu.edu|ニューヨーク大学コンピュータ・サイエンス学科博士課程|
|サイト管理者|<img src="https://pbs.twimg.com/profile_images/673997980370927616/vMXf545j_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/ebetica">Zeming Lin</a><br>zl2799@nyu.edu|ニューヨーク大学コンピュータ・サイエンス学科博士課程|


<!--
|採点者|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Serkan Karakulak <br>sk7685@nyu.edu|
|採点者|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Raghav Jajodia <br>rj1408@nyu.edu|
|採点者|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Priyank Pathak <br>pp1953@nyu.edu|
|採点者|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Chiao-Hsun Wang <br>chw371@nyu.edu|
|採点者|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Pedro Vidal<br>pmh314@nyu.edu|
|採点者|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Bixing Yan <br>by783@nyu.edu|
-->


## 注意事項

このサイトにあるテキストの元はニューヨーク大学の学生のレクチャー・ノートのです。日本語の翻訳は複数のボランティアによって翻訳されたものであるため、言葉遣い・訳語・スタイルが統一されてないことがあります。

また、誤訳、翻訳漏れ、入力ミスもあるかもしれません。それに気づく場合、[GitHub](https://github.com/Atcold/pytorch-Deep-Learning/pulls)にプルリクエストを提出し、タイトルに`[JA]`(和訳に関わるもの)を記載していただけると嬉しいです。
