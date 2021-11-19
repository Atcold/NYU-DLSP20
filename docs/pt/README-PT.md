<!-- Deep Learning (with PyTorch)
-->
# Aprendizagem Profunda (com PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

<!-- This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format.
-->
Este repositório de *notebooks* possui uma [página web complementar](https://atcold.github.io/pytorch-Deep-Learning/es/), onde todo o material do curso pode ser encontrado em formato textual e em vídeo.

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese - Bengali - Hungarian -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md) &nbsp; [🇧🇩](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/bn/README-BN.md) &nbsp; [🇭🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/hu/README-HU.md)

<!-- Getting started
-->
# Começando

<!-- To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
The following instruction would work as is for Mac or Ubuntu Linux users, Windows users would need to install and work in the [Git BASH](https://gitforwindows.org/) terminal.
-->
Para poder seguir os exercícios, você precisa ter um computador com Miniconda (uma versão minimalista do Anaconda) e vários pacotes Python instalados.
As instruções a seguir funcionarão para os usuários de Mac ou Ubuntu Linux. Os usuários Windows precisarão instalar e trabalhar em um terminal [Git BASH](https://gitforwindows.org/).

<!-- Download and install Miniconda
-->
## Download e instalação do Miniconda

<!-- Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system.
-->
Vá à [página web do Anaconda](https://conda.io/miniconda.html).
Faça o download e instale *a última* versão do Miniconda para *Python* 3.7 para seu sistema operacional.

<!-- wget <http:// link to miniconda>
-->
```bash
wget <http:// url a miniconda>
sh <miniconda*.sh>
```

<!-- Check-out the git repository with the exercise
-->
## Clone o repositório git contendo os exercícios

<!-- nce Miniconda is ready, checkout the course repository and proceed with setting up the environment:
-->
Uma vez que a instalação do Miniconda esteja concluída, baixe o repositório do curso faça a configuração do ambiente:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```

<!-- Create isolated Miniconda environment
-->
## Crie um ambiente Miniconda isolado

<!-- Change directory (`cd`) into the course folder, then type:
-->
Mude o diretório (`cd`) para a pasta do curso, e digite:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

<!-- Start Jupyter Notebook or JupyterLab
-->
## Inicie uma sessão Jupyter Notebook ou JupyterLab

<!-- Start from terminal as usual:
-->
Começe a partir do terminal, como padrão:

```bash
jupyter lab
```

<!-- Or, for the classic interface:
-->
Ou, para a interface clássica:

```bash
jupyter notebook
```

<!-- Notebooks visualisation
-->
## Visualização de notebooks

<!-- *Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.
-->
Os *Jupyter Notebooks* irão ser utilizados nas aulas para a exploração e visualização interativa de dados.

<!-- We use dark styles for both *GitHub* and *Jupyter Notebook*.
You should try to do the same, or they will look ugly.
JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface.
To see the content appropriately in the classic interface install the following:
-->
Utilizamos estilos escuros para *GitHub* e *Jupyter Notebook*.
Deveria tentar seguir o mesmo padrão, ou ficarão feios.
JupyterLab tem disponível um tema escuro, sendo que você somente precisará instalar alguma coisa adicional se desejar utilizar a interface clássica dos notebooks.
Para ver o conteúdo adequadamente na interface clássica, instale o seguinte:

<!--  - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.
-->
 - [Design escuro para *Jupyter Notebook*](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [Design escuro para *GitHub*](https://userstyles.org/styles/37035/github-dark) e descomente o seginte trecho de código `invert #fff to # 181818`.
