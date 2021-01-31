---
layout: default
title: APRENDIZAGEM PROFUNDA
author: Alfredo Canziani
lang-ref: home
lang: pt
---

**DS-GA 1008 · PRIMAVERA 2020 · [CENTRO DE CIÊNCIA DE DADOS DA NYU](http://cds.nyu.edu/)**

| INSTRUTORES | Yann LeCun & Alfredo Canziani |
| AULAS    | Segundas-feiras 16:55 – 18:35, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| PRÁTICAS    | Terças-feiras 19:10 – 20:00, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| FÓRUM         | [r/NYU_DeepLearning](https://www.reddit.com/r/NYU_DeepLearning/) |
| MATERIAL     | [Google Drive](https://bitly.com/DLSP20), [Notebooks](https://github.com/Atcold/pytorch-Deep-Learning) |


## Descrição

Este curso trata das técnicas mais recentes em aprendizagem profunda e aprendizagem de representação, com foco em aprendizagem profunda supervisionada e não supervisionada, métodos de incorporação, aprendizagem métrica, redes convolucionais e recorrentes, com aplicações para visão computacional, compreensão de linguagem natural e reconhecimento de fala. Os pré-requisitos incluem: [DS-GA 1001 Introdução à Ciência de Dados](https://cds.nyu.edu/academics/ms-curriculum/) ou um curso de aprendizado de máquina de pós-graduação.

## Aulas

**Legenda**: 🖥 slides, 📓 Jupyter notebook, 🎥 vídeo do YouTube.

<table>
<!-- =============================== HEADER ================================ -->
  <thead>
    <tr>
      <th>Semana</th>
      <th align="left">Formato</th>
      <th align="left">Título</th>
      <th align="left">Recursos</th>
    </tr>
  </thead>
  <tbody>
<!-- =============================== SEMANA 1 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week01/01">①</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week01/01-1">História e motivação</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week01/01-2">Evolução e DL</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week01/01-3">Redes neurais (NN)</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week02/02">②</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week02/02-1">SGD e backprop</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
        <a href="https://www.youtube.com/watch?v=d9vdh3b787Y">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week02/02-2">Backprop na prática</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week02/02-3">Treinamento de NNs</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=WAn6lip5oWk">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week03/03">③</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week03/03-1">Transformação de parâmetros</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
        <a href="https://youtu.be/FW5gFiJb-ig">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week03/03-2">CNN</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week03/03-3">Propriedades de sinais naturais</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
        <a href="https://youtu.be/kwPWpVverkw">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="{{site.baseurl}}/pt/week04/04">④</a></td>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week04/04-1">Convoluções em 1D</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
        <a href="https://youtu.be/OrBEon3VlQg">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week05/05">⑤</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week05/05-1">Otimização I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
        <a href="https://youtu.be/--NZb480zlg">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week05/05-2">Otimização II</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week05/05-3">CNN, autograd</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/03-autograd_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/extra/b-custom_grads.ipynb">📓</a>
        <a href="https://youtu.be/eEzCZnOFU1w">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 6 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week06/06">⑥</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week06/06-1">Aplicações de CNNs</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1opT7lV0IRYJegtZjuHsKhlsM5L7GpGL1">🖥️</a>
        <a href="https://drive.google.com/open?id=1sdeVBC3nuh5Zkm2sqzdScEicRvLc_v-F">🖥️</a>
        <a href="https://youtu.be/ycbMGyCPzvE">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week06/06-2">RNNs e atenção</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week06/06-3">Treinando RNNs</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/08-seq_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/09-echo_data.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/04%20-%20RNN.pdf">🖥️</a>
        <a href="https://youtu.be/8cAffg2jaT0">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week07/07">⑦</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week07/07-1">Modelos Baseados em Energia</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1z8Dz1YtkOEJpU-gh5RIjORs3GGqkYJQa">🖥️</a>
        <a href="https://youtu.be/tVwV14YkbYs">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week07/07-2">SSL, EBM</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week07/07-3">Autocodificadores</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/10-autoencoder.ipynb">📓</a>
        <a href="https://youtu.be/bggWQ14DD9M">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 8 ================================ -->
<tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week08/08">⑧</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week08/08-1">Métodos constrativos</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Zo_PyBEO6aNt0GV74kj8MQL7kfHdIHYO">🖥️</a>
        <a href="https://youtu.be/ZaVP2SY23nc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week08/08-2">Latente regularizado</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week08/08-3">Treinando VAEs</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/11-VAE.ipynb">📓</a>
        <a href="https://youtu.be/7Rb4s9wNOmc">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 9 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week09/09">⑨</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week09/09-1">Esparsidade</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1wJRzhjSqlrSqEpX4Omagb_gdIkQ5f-6K">🖥️</a>
        <a href="https://youtu.be/Pgct8PKV7iw">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week09/09-2">Modelos do mundo, GANs</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week09/09-3">Treinando GANs</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/pytorch/examples/tree/master/dcgan">📓</a>
        <a href="https://youtu.be/xYc11zyZ26M">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 10 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week10/10">⑩</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week10/10-1">CV SSL I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=16lsnDN2HIBTcRucbVKY5B_U16c0tNQhR">🖥️</a>
        <a href="https://youtu.be/0KeR6i1_56g">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week10/10-2">CV SSL II</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week10/10-3">Controle preditivo</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/09%20-%20Controller%20learning.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/14-truck_backer-upper.ipynb">📓</a>
        <a href="https://youtu.be/A3klBqEWR-I">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 11 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week11/11">⑪</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week11/11-1">Ativações</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1AzFVLG7D4NK6ugh60f0cJQGYF5OL2sUB">🖥️</a>
        <a href="https://drive.google.com/file/d/1rkiZy0vjZqE2w7baVWvxwfAGae0Eh1Wm">🖥️</a>
        <a href="https://drive.google.com/file/d/1tryOlVAFmazLLZusD2-UfReFMkPk5hPk">🖥️</a>
        <a href="https://youtu.be/bj1fh3BvqSU">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week11/11-2">Perdas</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week11/11-3">PPUU</a></td>
      <td>
        <a href="http://bit.ly/PPUU-slides">🖥️</a>
        <a href="http://bit.ly/PPUU-code">📓</a>
        <a href="https://youtu.be/VcrCr-KNBHc">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 12 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week12/12">⑫</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week12/12-1">DL para PLN I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/149m3wRavTp4DQZ6RJTej8KP8gv4jnkPW/">🖥️</a>
        <a href="https://youtu.be/6D4EWKJgNn0">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week12/12-2">DL para PLN II</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week12/12-3">Atenção & transformador</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/10%20-%20Attention%20%26%20transformer.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/15-transformer.ipynb">📓</a>
        <a href="https://youtu.be/f01J0Dri-6k">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 13 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week13/13">⑬</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week13/13-1">GCNs I</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1oq-nZE2bEiQjqBlmk5_N_rFC8LQY0jQr/">🖥️</a>
        <a href="https://youtu.be/Iiv9R6BjxHM">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week13/13-2">GCNs II</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week13/13-3">GCNs III</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/11%20-%20GCN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/16-gated_GCN.ipynb">📓</a>
        <a href="https://youtu.be/2aKXWqkbpWg">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 14 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="{{site.baseurl}}/pt/week14/14">⑭</a></td>
      <td rowspan="2">Aula</td>
      <td><a href="{{site.baseurl}}/pt/week14/14-1">Predição Estruturada</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1qBu-2hYWaGYEXeX7kAU8O4S2RZ1hMjsk/">🖥️</a>
        <a href="https://youtu.be/gYayCG6YyO8">🎥</a>
      </td>
    </tr>
    <tr><td><a href="{{site.baseurl}}/pt/week14/14-2">Métodos gráficos</a></td></tr>
    <tr>
      <td rowspan="1">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week14/14-3">Regularização e Bayesiana</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/07%20-%20Regularisation.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/12-regularization.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/08%20-%20Bayesian%20NN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/13-bayesian_nn.ipynb">📓</a>
        <a href="https://youtu.be/DL7iew823c0">🎥</a>
      </td>
    </tr>
<!-- =============================== SEMANA 15 =============================== -->
    <tr>
      <td rowspan="2" align="center"><a href="{{site.baseurl}}/pt/week15/15">⑮</a></td>
      <td rowspan="2">Prática</td>
      <td><a href="{{site.baseurl}}/pt/week15/15-1">Inferência para Variável Latente EBMs</a></td>
      <td rowspan="1">
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf">🖥️</a>
        <a href="https://youtu.be/sbhr2wjU1-I">🎥</a>
      </td>
    </tr>
    <tr>
      <td><a href="{{site.baseurl}}/pt/week15/15-2">Treinando Variável Latente EBMs</a></td>
      <td rowspan="1">
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf">🖥️</a>
        <a href="https://youtu.be/XLSb1Cs1Jao">🎥</a>
      </td>
    </tr>
</tbody>
</table>

## Pessoas

| Cargo | Foto | Contato | Sobre |
|:-----|:-----:|:--------|:------|
|Instrutor|<img src="../images/Yann.png" width="100" height="100">|<a href="https://twitter.com/ylecun">Yann LeCun</a><br>yann@cs.nyu.edu|Silver Professor em CS<br> na NYU e ganhador <br>do Prêmio Turing|
|Instrutor|<img src="https://avatars1.githubusercontent.com/u/2119355" width="100" height="100">|<a href="https://twitter.com/alfcnz">Alfredo Canziani</a><br>canziani@nyu.edu|Professor Assistente em Ciência da Computação na NYU|
|Asistente|<img src="https://pbs.twimg.com/profile_images/1186879808845860864/czRv3g1G_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/marikgoldstein">Mark Goldstein</a><br>goldstein@nyu.edu|Estudante de doutorado em Ciência da Computação na NYU|
|Webmaster|<img src="https://pbs.twimg.com/profile_images/673997980370927616/vMXf545j_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/ebetica">Zeming Lin</a><br>zl2799@nyu.edu|Estudante de doutorado em Ciência da Computação na NYU|

