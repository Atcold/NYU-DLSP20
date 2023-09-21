# NYU Deep Learning Spring 2020 (NYU-DLSP20) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/NYU-DLSP20/master)

This notebook repository now has a [companion website](https://atcold.github.io/NYU-DLSP20/), where all the course material can be found in video and textual format.

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese -->
[🇬🇧](https://github.com/Atcold/NYU-DLSP20/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/pt/README-PT.md) &nbsp; [🇭🇺](https://github.com/Atcold/NYU-DLSP20/blob/master/docs/hu/README-HU.md)


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
git clone https://github.com/Atcold/NYU-DLSP20.git
```


## Create isolated Miniconda environment

Change directory (`cd`) into the course folder, then type:

```bash
# cd NYU-DLSP20
conda env create -f environment.yml
source activate NYU-DL
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
