# Deep Learning (with PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)![hu](https://img.shields.io/badge/hu-1%25%202%2F104-red) ![sr](https://img.shields.io/badge/sr-1%25%202%2F104-red) ![ja](https://img.shields.io/badge/ja-53%25%2056%2F104-yellow) ![tr](https://img.shields.io/badge/tr-47%25%2049%2F104-yellow) ![en](https://img.shields.io/badge/en-100%25%20104%2F104-green) ![ru](https://img.shields.io/badge/ru-11%25%2012%2F104-red) ![zh](https://img.shields.io/badge/zh-57%25%2060%2F104-yellow) ![bn](https://img.shields.io/badge/bn-10%25%2011%2F104-red) ![it](https://img.shields.io/badge/it-43%25%2045%2F104-yellow) ![fr](https://img.shields.io/badge/fr-53%25%2056%2F104-yellow) ![vi](https://img.shields.io/badge/vi-6%25%207%2F104-red) ![fa](https://img.shields.io/badge/fa-20%25%2021%2F104-red) ![ko](https://img.shields.io/badge/ko-53%25%2056%2F104-yellow) ![ar](https://img.shields.io/badge/ar-38%25%2040%2F104-yellow) ![pt](https://img.shields.io/badge/pt-6%25%207%2F104-red) ![es](https://img.shields.io/badge/es-54%25%2057%2F104-yellow) 

















This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format.

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md) &nbsp; [🇭🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/hu/README-HU.md)


# Getting started

To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
The following instruction would work as is for Mac or Ubuntu Linux users, Windows users would need to install and work in the [Git BASH](https://gitforwindows.org/) terminal.


## Download and install Miniconda

Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```


## Check-out the git repository with the exercise

Once Miniconda is ready, checkout the course repository and proceed with setting up the environment:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


## Create isolated Miniconda environment

Change directory (`cd`) into the course folder, then type:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


## Start Jupyter Notebook or JupyterLab

Start from terminal as usual:

```bash
jupyter lab
```

Or, for the classic interface:

```bash
jupyter notebook
```


## Notebooks visualisation

*Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.

We use dark styles for both *GitHub* and *Jupyter Notebook*.
You should try to do the same, or they will look ugly.
JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface.
To see the content appropriately in the classic interface install the following:

 - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.
