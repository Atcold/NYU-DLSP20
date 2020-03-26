---
layout: default
title: APPRENDIMENTO PROFONDO
author: Alfredo Canziani
lang-ref: home
lang: it
---

**DS-GA 1008 · PRIMAVERA 2020 · [NYU CENTER FOR DATA SCIENCE](http://cds.nyu.edu/)**

| ISTRUTTORI  | Yann LeCun & Alfredo Canziani |
| LEZIONI     | Lunedì 16:55 – 18:35, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| PRACTICA    | Martedì 19:10 – 20:00, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| [PIAZZA](https://piazza.com/nyu/spring2020/dsga1008/home)      | Codice d'accesso: `DLSP20` |
| MATERIALE   | [Google Drive](https://bitly.com/DLSP20), [Notebooks](https://github.com/Atcold/pytorch-Deep-Learning) |


## Description

Questo corso tratta delle ultime tecniche in apprendimento profondo (DL, Deep learning) e
apprendimento della rappresentazione (representation learning), concentrandosi
su apprendimento profondo supervisionato e non-supervisionato, metodi di
embedding, apprendimento metrico (metric learning), reti convoluzionali e
ricorrenti (CNN, Convolutional Neural Network); RNN, Recurrent Neural Network),
con applicazioni di visione artificiale (computer vision), comprendimento del
linguaggio naturale (NLU, Natural Language Understanding) e
riconoscimento vocale (Speech Processing).
I prerequisiti del corso includono: [DS-GA 1001 Intro to Data
Science](https://cds.nyu.edu/academics/ms-curriculum/) o un corso di machine
learning universitario.


## Lezioni

**Legenda**: 🖥 slide, 📓 Jupyter notebook, 🎥 video di YouTube.

<table>
<!-- =============================== HEADER ================================ -->
  <thead>
    <tr>
      <th>Settimana</th>
      <th align="left">Formato</th>
      <th align="left">Titolo</th>
      <th align="left">Risorse</th>
    </tr>
  </thead>
  <tbody>
<!-- =============================== WEEK 1 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week01/01">①</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="it/week01/01-1">Storia e motivazione</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="it/week01/01-2">Evoluzione e apprendimento profondo (DL, Deep Learning)</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="it/week01/01-3">Reti Neurali (NN, Neural Network)</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week02/02">②</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="it/week02/02-1">SGD e retropropagazione (backpropagation)</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
        <a href="https://www.youtube.com/watch?v=d9vdh3b787Y">🎥</a>
      </td>
    </tr>
    <tr><td><a href="it/week02/02-2">Retropropagazione in pratica</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="it/week02/02-3">Addestramento di reti neurali</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=WAn6lip5oWk">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week03/03">③</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="it/week03/03-1">Trasformazione dei parametri</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
        <a href="https://youtu.be/FW5gFiJb-ig">🎥</a>
      </td>
    </tr>
    <tr><td><a href="it/week03/03-2">CNN</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="it/week03/03-3">Proprietà dei segnali naturali</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
        <a href="https://youtu.be/kwPWpVverkw">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="it/week04/04">④</a></td>
      <td rowspan="1">Pratica</td>
      <td><a href="it/week04/04-1">Convoluzioni 1D</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
        <a href="https://youtu.be/OrBEon3VlQg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week05/05">⑤</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="it/week05/05-1">Ottimizzazione I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
        <a href="https://youtu.be/--NZb480zlg">🎥</a>
      </td>
    </tr>
    <tr><td><a href="it/week05/05-2">Ottimizzazione II</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="it/week05/05-3">CNN, autograd</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/03-autograd_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/extra/b-custom_grads.ipynb">📓</a>
        <a href="https://youtu.be/eEzCZnOFU1w">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 6 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week06/06">⑥</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="it/week06/06-1"></a>-</td>
      <td rowspan="2">
        <a href=""></a>
      </td>
    </tr>
    <tr><td><a href="it/week06/06-2"></a>-</td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="it/week06/06-3"></a>-</td>
      <td>
      </td>
    </tr>
<!-- =============================== WEEK 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week07/07"></a>⑦</td>
      <td rowspan="2">Lezione</td>
      <td><a href="it/week07/07-1">Modelli a Energia (Energy-Based Models)</a>-</td>
      <td rowspan="2">
        <a href=""></a>
      </td>
    </tr>
    <tr><td><a href="it/week07/07-2"></a>SSL, EBM</td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="it/week07/07-3">Auto-codificatori (Autoencoder)</a></td>
      <td>
        <a href="https://drive.google.com/file/d/1FEleglSDblyrSpHdGhaDydEQI36Rq5uB/">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/10-autoencoder.ipynb">📓</a>
      </td>
    </tr>
  </tbody>
</table>


## People

| Role | Photo | Contact | About |
|:-----|:-----:|:--------|:------|
|Instructor|<img src="images/Yann.png" width="100" height="100">|<a href="https://twitter.com/ylecun">Yann LeCun</a><br>yann@cs.nyu.edu|Silver Professor in CS a NYU<br>and vincitore del Turing Award|
|Instructor|<img src="https://avatars1.githubusercontent.com/u/2119355" width="100" height="100">|<a href="https://twitter.com/alfcnz">Alfredo Canziani</a><br>canziani@nyu.edu|Professore in CS a NYU|
|Assistant|<img src="https://pbs.twimg.com/profile_images/1186879808845860864/czRv3g1G_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/marikgoldstein">Mark Goldstein</a><br>goldstein@nyu.edu|Dottorando in CS at NYU|
|Webmaster|<img src="https://pbs.twimg.com/profile_images/673997980370927616/vMXf545j_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/ebetica">Zeming Lin</a><br>zl2799@nyu.edu|Dottorando in CS at NYU|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Serkan Karakulak <br>sk7685@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Raghav Jajodia <br>rj1408@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Priyank Pathak <br>pp1953@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Chiao-Hsun Wang <br>chw371@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Pedro Vidal<br>pmh314@nyu.edu|
|Grader|<img src="https://st3.depositphotos.com/13159112/17145/v/450/depositphotos_171453724-stock-illustration-default-avatar-profile-icon-grey.jpg" width="100" height="100">|Bixing Yan <br>by783@nyu.edu|
