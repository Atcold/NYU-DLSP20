---
layout: default
title: APPRENDIMENTO PROFONDO
author: Alfredo Canziani
lang-ref: home
lang: it
translation-date: 26 Mar 2020
translator: Nantas Nardelli
---

**DS-GA 1008 · PRIMAVERA 2020 · [NYU CENTER FOR DATA SCIENCE](http://cds.nyu.edu/)**

| ISTRUTTORI  | Yann LeCun & Alfredo Canziani |
| LEZIONI     | Lunedì 16:55 – 18:35, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| PRATICA    | Martedì 19:10 – 20:00, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| FORUM       | [r/NYU_DeepLearning](https://www.reddit.com/r/NYU_DeepLearning/) |
| MATERIALE   | [Google Drive](https://bitly.com/DLSP20), [Notebooks](https://github.com/Atcold/pytorch-Deep-Learning) |


## Description

Questo corso tratta delle ultime tecniche in apprendimento profondo (DL, Deep learning) e apprendimento della rappresentazione (representation learning), concentrandosi su apprendimento profondo supervisionato e non-supervisionato, metodi di embedding, apprendimento metrico (metric learning), reti convoluzionali e ricorrenti (CNN, Convolutional Neural Network); RNN, Recurrent Neural Network), con applicazioni di visione artificiale (computer vision), comprendimento del linguaggio naturale (NLU, Natural Language Understanding) e riconoscimento vocale (Speech Processing).  I prerequisiti del corso includono: [DS-GA 1001 Intro to Data Science](https://cds.nyu.edu/academics/ms-curriculum/) o un corso di machine learning universitario.

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
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/it/week01/01">①</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week01/01-1">Storia e motivazione</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week01/01-2">Evoluzione e apprendimento profondo (DL, Deep Learning)</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week01/01-3">Reti Neurali (NN, Neural Network)</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/it/week02/02">②</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week02/02-1">SGD e retropropagazione (backpropagation)</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
        <a href="https://www.youtube.com/watch?v=d9vdh3b787Y">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week02/02-2">Retropropagazione in pratica</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week02/02-3">Addestramento di reti neurali</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=WAn6lip5oWk">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/it/week03/03">③</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week03/03-1">Trasformazione dei parametri</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
        <a href="https://youtu.be/FW5gFiJb-ig">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week03/03-2">CNN</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week03/03-3">Proprietà dei segnali naturali</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
        <a href="https://youtu.be/kwPWpVverkw">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="{{site.baseurl}}/it/week04/04">④</a></td>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week04/04-1">Convoluzioni 1D</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
        <a href="https://youtu.be/OrBEon3VlQg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/it/week05/05">⑤</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week05/05-1">Ottimizzazione I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
        <a href="https://youtu.be/--NZb480zlg">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week05/05-2">Ottimizzazione II</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week05/05-3">CNN, autograd</a></td>
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
      <td><a href="{{site.baseurl}}/it/week06/06-1">Applicazioni di reti convoluzionali</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1opT7lV0IRYJegtZjuHsKhlsM5L7GpGL1">🖥️</a>
        <a href="https://drive.google.com/open?id=1sdeVBC3nuh5Zkm2sqzdScEicRvLc_v-F">🖥️</a>
        <a href="https://youtu.be/ycbMGyCPzvE">🎥</a>
      </td>
    </tr>
    <tr><td><a href="it/week06/06-2">RNNs, GRUs, LSTMs, Attenzione, Seq2Seq, e Reti di Memoria</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week06/06-3">Architettura delle RNN e modelli LSTM</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/04%20-%20RNN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/08-seq_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/09-echo_data.ipynb">📓</a>
        <a href="https://youtu.be/8cAffg2jaT0">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week07/07">⑦</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week07/07-1">Modelli ad energia (EBM, Energy Based Models)</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1z8Dz1YtkOEJpU-gh5RIjORs3GGqkYJQa">🖥️</a>
        <a href="https://youtu.be/tVwV14YkbYs">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week07/07-2">SSL, EBM con dettagli ed esempi</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week07/07-3">Introduzione agli autoencoder</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/10-autoencoder.ipynb">📓</a>
        <a href="https://youtu.be/bggWQ14DD9M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 8 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week08/08">⑧</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week08/08-1">Metodi contrastivi nei modelli ad energia</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Zo_PyBEO6aNt0GV74kj8MQL7kfHdIHYO">🖥️</a>
        <a href="https://youtu.be/ZaVP2SY23nc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week08/08-2">Modelli ad energia a variabile latente regolarizzata</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week08/08-3">Modelli generativi - autoencoder variazionali</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/11-VAE.ipynb">📓</a>
        <a href="https://youtu.be/7Rb4s9wNOmc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 9 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week09/09">⑨</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week09/09-1">Autoencoder discriminativi ricorrenti sparsi</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1wJRzhjSqlrSqEpX4Omagb_gdIkQ5f-6K">🖥️</a>
        <a href="https://youtu.be/Pgct8PKV7iw">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week09/09-2">Modelli della realtà e reti avversarie generative</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week09/09-3">Reti avversarie generative</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/pytorch/examples/tree/master/dcgan">📓</a>
        <a href="https://youtu.be/xYc11zyZ26M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 10 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week10/10">⑩</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week10/10-1">Apprendimento auto-supervisionato - Compiti di pretesto</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=16lsnDN2HIBTcRucbVKY5B_U16c0tNQhR">🖥️</a>
        <a href="https://youtu.be/0KeR6i1_56g">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week10/10-2">Apprendimento auto-supervisionato - ClusterFit e PIRL</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week10/10-3">Il controllore per la retromarcia di un camion</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/09%20-%20Controller%20learning.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/14-truck_backer-upper.ipynb">📓</a>
        <a href="https://youtu.be/A3klBqEWR-I">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 11 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="it/week11/11">⑪</a></td>
      <td rowspan="2">Lezione</td>
      <td><a href="{{site.baseurl}}/it/week11/11-1">Funzioni di attivazione e di perdita (parte 1)</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1AzFVLG7D4NK6ugh60f0cJQGYF5OL2sUB">🖥️</a>
        <a href="https://drive.google.com/file/d/1rkiZy0vjZqE2w7baVWvxwfAGae0Eh1Wm">🖥️</a>
        <a href="https://drive.google.com/file/d/1tryOlVAFmazLLZusD2-UfReFMkPk5hPk">🖥️</a>
        <a href="https://youtu.be/bj1fh3BvqSU">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/it/week11/11-2">Funzioni di perdita (cont.) e funzioni di perdita per i modelli ad energia</a></td></tr>
    <tr>
      <td rowspan="1">Pratica</td>
      <td><a href="{{site.baseurl}}/it/week11/11-3">Articolo "Prediction and Policy learning Under Uncertainty" (PPUU)</a></td>
      <td>
        <a href="http://bit.ly/PPUU-slides">🖥️</a>
        <a href="http://bit.ly/PPUU-code">📓</a>
        <a href="https://youtu.be/VcrCr-KNBHc">🎥</a>
      </td>
    </tr>
  </tbody>
</table>




## People

| Role | Photo | Contact | About |
|:-----|:-----:|:--------|:------|
|Instructor|<img src="../images/Yann.png" width="100" height="100">|<a href="https://twitter.com/ylecun">Yann LeCun</a><br>yann@cs.nyu.edu|Silver Professor in CS a NYU<br>and vincitore del Turing Award|
|Instructor|<img src="https://avatars1.githubusercontent.com/u/2119355" width="100" height="100">|<a href="https://twitter.com/alfcnz">Alfredo Canziani</a><br>canziani@nyu.edu|Professore in CS a NYU|
|Assistant|<img src="https://pbs.twimg.com/profile_images/1186879808845860864/czRv3g1G_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/marikgoldstein">Mark Goldstein</a><br>goldstein@nyu.edu|Dottorando in CS at NYU|
|Webmaster|<img src="https://pbs.twimg.com/profile_images/673997980370927616/vMXf545j_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/ebetica">Zeming Lin</a><br>zl2799@nyu.edu|Dottorando in CS at NYU|
