# 深層学習 (with PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)
<!-- This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format. -->
この講義で用いられる資料は全て、ビデオあるいはテキスト形式で[付随しているウェブサイト](https://atcold.github.io/pytorch-Deep-Learning/)に全て含まれています。

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md)

<!-- # Getting started -->
# 始め方

<!-- To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.                       -->
<!-- The following instruction would work as is for Mac or Ubuntu Linux users, Windows users would need to install and work in the [Git BASH](https://gitforwindows.org/) terminal. -->
演習を始めるために、Miniconda (Anaconda の最小バージョン) といくつかの Python パッケージがインストールされた PC を用意する必要があります。
以下の説明は Mac や Ubuntu (Linux) を使用している場合は正しく動作します。Windows を使用している場合は [Git BASH](https://gitforwindows.org/) をインストールする必要があります。

<!-- ## Download and install Miniconda -->
## Miniconda をインストールする

<!-- Please go to the [Anaconda website](https://conda.io/miniconda.html).                           -->
<!-- Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system. -->
[Anaconda のウェブサイト](https://conda.io/miniconda.html) にアクセスし、
使用してる OS の、*Python* 3.7 を用いている最新のバージョンをインストールしてください。

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```

<!-- ## Check-out the git repository with the exercise -->
## 演習用の Git リポジトリをチェックアウトする

<!-- Once Miniconda is ready, checkout the course repository and proceed with setting up the environment: -->
Minionca を準備したあとは、この講義のリポジトリをチェックアウトし、環境構築を行います。

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```

<!-- ## Create isolated Miniconda environment -->
## 独立した Miniconda の環境を作成する

<!-- Change directory (`cd`) into the course folder, then type: -->
`cd` コマンドを用いてこのリポジトリのルートディレクトリに入り、以下のコマンドを実行します。

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

<!-- ## Start Jupyter Notebook or JupyterLab -->
## Jupyter Notebook または JupyterLab を起動する

<!-- Start from terminal as usual: -->
次のコマンドを実行してターミナルから起動します. 

```bash
jupyter lab
```

<!-- Or, for the classic interface: -->
クラシックなインターフェイスを使う場合は、かわりに以下を実行します。

```bash
jupyter notebook
```

<!-- ## Notebooks visualisation -->
## ノートブックの可視化

<!-- *Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation. -->
この講義を通して、*Jupyter Notebooks* はインタラクティブなデータの探索と可視化を行うために用いられます。

<!-- We use dark styles for both *GitHub* and *Jupyter Notebook*.                                                                              -->
<!-- You should try to do the same, or they will look ugly.                                                                                    -->
<!-- JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface. -->
<!-- To see the content appropriately in the classic interface install the following:                                                          -->
私たちは *Github* と *Jupyter Notebook* の両方でダークテーマを用いています。
デフォルトのテーマは見苦しいため、同じテーマを使用してみてください。
JupyterLab は標準でダークテーマが選択可能です。クラシックな Jupyter Notebook を用いている場合のみ、
以下の 2 つをインストールする必要があります。

 <!-- - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);                                    -->
 <!-- - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block. -->
 - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) (コード中にある `invert #fff to #181818` はコメントアウトしてください)
