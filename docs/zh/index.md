---
layout: default
title: 深度学习
author: Alfredo Canziani
lang-ref: home
lang: zh
translation-date: 24 Feb 2020
translator: Mingyang Zhao
---

**DS-GA 1008 · 2020 春季 · [纽约大学数据科学中心](http://cds.nyu.edu/)**

| 指导教师          | Yann LeCun 和 Alfredo Canziani  |
| 讲座课            | 周一 16:55 – 18:35, [GCASL C95] |
| 动手做            | 周二 19:10 – 20:00, [GCASL C95] |
| [PIAZZA 讨论区]   | 验证码: `DLSP20`                |
| 资料              | [Google 云端硬盘], [Notebooks]  |

<!-- Links -->
[GCASL C95]: http://libzuorary.nyu.edu/services/campus-media/classrooms/gcasl-c95/
[PIAZZA 讨论区]: https://piazza.com/nyu/spring2020/dsga1008/home
[Google 云端硬盘]: https://bitly.com/DLSP20
[Notebooks]: (https://github.com/Atcold/pytorch-Deep-Learning)


## 简介

本课程涉及深度学习和表示学习的最新技术，重点包括监督式深度学习和无监督深度学习、（词）嵌入、度量学习、卷积和递归网络，以及在计算机视觉、自然语言理解和语音识别方面的应用。先修课程包括：[DS-GA 1001 数据科学入门] 或一门研究生级别的机器学习课程。

<!-- Links -->
[DS-GA 1001 数据科学入门]: https://cds.nyu.edu/academics/ms-curriculum/


## 课程

**图例**: 🖥 幻灯片, 📓 Jupyter notebook, 🎥 YouTube 视频.

<table>
<!-- =============================== HEADER ================================ -->
  <thead>
    <tr>
      <th>周数</th>
      <th align="left">形式</th>
      <th align="left">题目</th>
      <th align="left">资源</th>
    </tr>
  </thead>
  <tbody>
<!-- =============================== WEEK 1 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/zh/week01/01">①</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="{{site.baseurl}}/zh/week01/01-1">历史及动力</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/zh/week01/01-2">发展及深度学习</a></td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="{{site.baseurl}}/zh/week01/01-3">神经网络 NN</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/zh/week02/02">②</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="{{site.baseurl}}/zh/week02/02-1">随机梯度下降 SGD 及反向传播</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/zh/week02/02-2">反向传播详解</a></td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="{{site.baseurl}}/zh/week02/02-3">训练神经网络</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
      </td>
    </tr>
<!-- =============================== WEEK 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/zh/week03/03">③</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="{{site.baseurl}}/zh/week03/03-1">参数转换</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/zh/week03/03-2">卷积神经网络 CNN</a></td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="{{site.baseurl}}/zh/week03/03-3">自然信号的性质</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
      </td>
    </tr>
<!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="{{site.baseurl}}/zh/week04/04">④</a></td>
      <td rowspan="1">动手做</td>
      <td><a href="{{site.baseurl}}/zh/week04/04-1">一维卷积</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
      </td>
    </tr>
<!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/zh/week05/05"></a>⑤</td>
      <td rowspan="2">讲座</td>
      <td><a href="{{site.baseurl}}/zh/week05/05-1"></a>-</td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/zh/week05/05-2"></a>-</td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="{{site.baseurl}}/zh/week05/05-3"></a>-</td>
      <td>
      </td>
    </tr>
  </tbody>
</table>
<!-- =============================== WEEK 6 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week06/06">⑥</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="en/week06/06-1">卷积神经网络的用途</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1opT7lV0IRYJegtZjuHsKhlsM5L7GpGL1">🖥️</a>
        <a href="https://drive.google.com/open?id=1sdeVBC3nuh5Zkm2sqzdScEicRvLc_v-F">🖥️</a>
        <a href="https://youtu.be/ycbMGyCPzvE">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week06/06-2">循环神经网路和注意力</a></td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="en/week06/06-3">训练循环神经网路</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/08-seq_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/09-echo_data.ipynb">📓</a>
        <a href="https://youtu.be/8cAffg2jaT0">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week07/07">⑦</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="en/week07/07-1">能量基础模型</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1z8Dz1YtkOEJpU-gh5RIjORs3GGqkYJQa">🖥️</a>
        <a href="https://youtu.be/tVwV14YkbYs">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week07/07-2">自我监督学习(SSL)﹑能量基础模型(EBM)</a></td></tr>
    <tr>
      <td rowspan="1">Practicum</td>
      <td><a href="en/week07/07-3">自动编码器</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/10-autoencoder.ipynb">📓</a>
        <a href="https://youtu.be/bggWQ14DD9M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 8 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week08/08">⑧</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="en/week08/08-1">对比法</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Zo_PyBEO6aNt0GV74kj8MQL7kfHdIHYO">🖥️</a>
        <a href="https://youtu.be/ZaVP2SY23nc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week08/08-2">对潜在进行正则化</a></td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="en/week08/08-3">训练变分自编码器</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/11-VAE.ipynb">📓</a>
        <a href="https://youtu.be/7Rb4s9wNOmc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 9 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week09/09">⑨</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="en/week09/09-1">稀疏性</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1wJRzhjSqlrSqEpX4Omagb_gdIkQ5f-6K">🖥️</a>
        <a href="https://youtu.be/Pgct8PKV7iw">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week09/09-2">世界模型﹑对抗性生成网络(GANs)</a></td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="en/week09/09-3">训练对抗性生成网络(GANs)</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/pytorch/examples/tree/master/dcgan">📓</a>
        <a href="https://youtu.be/xYc11zyZ26M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 10 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week10/10">⑩</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="en/week10/10-1">CV自我监督学习一</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=16lsnDN2HIBTcRucbVKY5B_U16c0tNQhR">🖥️</a>
        <a href="https://youtu.be/0KeR6i1_56g">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week10/10-2">CV自我监督学习二</a></td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="en/week10/10-3">有预测性的控制</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/09%20-%20Controller%20learning.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/14-truck_backer-upper.ipynb">📓</a>
        <a href="https://youtu.be/A3klBqEWR-I">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 11 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week11/11">⑪</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="en/week11/11-1">激活</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1AzFVLG7D4NK6ugh60f0cJQGYF5OL2sUB">🖥️</a>
        <a href="https://drive.google.com/file/d/1rkiZy0vjZqE2w7baVWvxwfAGae0Eh1Wm">🖥️</a>
        <a href="https://drive.google.com/file/d/1tryOlVAFmazLLZusD2-UfReFMkPk5hPk">🖥️</a>
        <a href="https://youtu.be/bj1fh3BvqSU">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week11/11-2">损失</a></td></tr>
    <tr>
      <td rowspan="1">动手做</td>
      <td><a href="en/week11/11-3">不确定性下的预测和策略学习(PPUU)</a></td>
      <td>
        <a href="http://bit.ly/PPUU-slides">🖥️</a>
        <a href="http://bit.ly/PPUU-code">📓</a>
        <a href="https://youtu.be/VcrCr-KNBHc">🎥</a>
      </td>
    </tr>
  </tbody>
</table>


## 人物

| 角式 | 相片 | 联络方式 | 关于 |
|:-----|:-----:|:--------|:------|
|讲师|<img src="images/Yann.png" width="100" height="100">|<a href="https://twitter.com/ylecun">Yann LeCun</a><br>yann@cs.nyu.edu|在紐約大學計算機科學部门的銀級教授<br>同時也是圖靈獎獲得者|
|讲师|<img src="https://avatars1.githubusercontent.com/u/2119355" width="100" height="100">|<a href="https://twitter.com/alfcnz">Alfredo Canziani</a><br>canziani@nyu.edu|紐約大學計算機科學部门的助教|
|助手|<img src="https://pbs.twimg.com/profile_images/1186879808845860864/czRv3g1G_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/marikgoldstein">Mark Goldstein</a><br>goldstein@nyu.edu|纽约大学计算机科学博士学生|
|网站管理员|<img src="https://pbs.twimg.com/profile_images/673997980370927616/vMXf545j_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/ebetica">Zeming Lin</a><br>zl2799@nyu.edu|纽约大学计算机科学博士学生|
|评分员|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Serkan Karakulak <br>sk7685@nyu.edu|
|评分员|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Raghav Jajodia <br>rj1408@nyu.edu|
|评分员|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Priyank Pathak <br>pp1953@nyu.edu|
|评分员|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Chiao-Hsun Wang <br>chw371@nyu.edu|
|评分员|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Pedro Vidal<br>pmh314@nyu.edu|
|评分员|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Bixing Yan <br>by783@nyu.edu|
