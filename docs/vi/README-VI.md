# Học sâu (với PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

Notebook này hiện đang được phát hành tại [trang web](https://atcold.github.io/pytorch-Deep-Learning/), nơi tất cả tài liệu của khóa học có thể được tìm thấy ở định dạng video hoặc văn bản.

<!-- Mandarin -->
<!--
🇨🇳 这份`README.md`的中文版本及网站可以在[这里](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md)找到.-->

<!-- Korean -->
<!--
🇰🇷 한국어 `README.md`는 [여기](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md)에서 확인하실 수 있습니다.
-->

<!-- Spanish -->
<!--
🇪🇸 La versión en Español de este `README.md` y el sitio web [se encuentran aquí](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md).-->

<!-- Italian -->
<!--
🇮🇹 La versione in italiano di questo `README.md` può essere trovata  [a questo indirizzo](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md).
-->
<!-- Turkish -->
<!--
🇹🇷 `README.md`'nin Türkçe çevirisi [bu](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) adreste bulunabilir.
-->
<!-- Japanese -->
<!--
🇯🇵 日本語版の `README.md` は  [ここ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) にあります.
-->

<!-- Arabic -->
<!--
🇸🇦 النسخة العربية من ملف `README.md`  [ar](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) والموقع الالكتروني.
-->

<!-- Vietnamese -->
<!-- Các bạn có thể tìm thấy phiên bản Tiếng Việt của `README.md` [Vi](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) tại đây!

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - Vietnamse-->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md)


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
