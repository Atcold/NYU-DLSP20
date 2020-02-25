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
| 实践课            | 周二 19:10 – 20:00, [GCASL C95] |
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
      <td rowspan="3" align="center"><a href="chapters/zh/01">①</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="chapters/zh/01-1">历史及动力</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="chapters/zh/01-2">发展及深度学习</a></td></tr>
    <tr>
      <td rowspan="1">实践</td>
      <td><a href="chapters/zh/01-3">神经网络 NN</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="chapters/zh/02">②</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="chapters/zh/02-1">随机梯度下降 SGD 及反向传播</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
      </td>
    </tr>
    <tr><td><a href="chapters/zh/02-2">反向传播详解</a></td></tr>
    <tr>
      <td rowspan="1">实践</td>
      <td><a href="chapters/zh/02-3">训练神经网络</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
      </td>
    </tr>
<!-- =============================== WEEK 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="chapters/zh/03">③</a></td>
      <td rowspan="2">讲座</td>
      <td><a href="chapters/zh/03-1">参数转换</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
      </td>
    </tr>
    <tr><td><a href="chapters/zh/03-2">卷积神经网络 CNN</a></td></tr>
    <tr>
      <td rowspan="1">实践</td>
      <td><a href="chapters/zh/03-3">自然信号的性质</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
      </td>
    </tr>
<!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="chapters/zh/04">④</a></td>
      <td rowspan="1">实践</td>
      <td><a href="chapters/zh/04-1">一维卷积</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
      </td>
    </tr>
<!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="chapters/zh/05"></a>⑤</td>
      <td rowspan="2">讲座</td>
      <td><a href="chapters/zh/05-1"></a>-</td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
      </td>
    </tr>
    <tr><td><a href="chapters/zh/05-2"></a>-</td></tr>
    <tr>
      <td rowspan="1">实践</td>
      <td><a href="chapters/zh/05-3"></a>-</td>
      <td>
      </td>
    </tr>
  </tbody>
</table>
