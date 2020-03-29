# 深度学习 (使用PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

这份笔记的仓库具有[同步网站](https://atcold.github.io/pytorch-Deep-Learning/zh/)，在那里您可以获得所有课程资料的视频与文本.


# 开始

为了能够完成练习，你需要为你的电脑安装Miniconda (Anaconda的精简版本)和一些Python包。以下说明步骤适用于Mac或者Ubuntu Linux用户，Windows用户需要安装[Git BASH](https://gitforwindows.org/)终端，并在该终端中完成操作。


## 下载并安装Miniconda

请前往[Anaconda网站](https://conda.io/miniconda.html)，下载并且安装适合你的操作系统的*最新*Miniconda版本。其中*Python*版本请选择3.8

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```


## 下载带有练习的git仓库

一旦你的Miniconda准备妥当，请下载课程的git仓库，同时建立Miniconda环境。

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


## 创建独立的Miniconda环境

进入课程目录(`cd`)， 然后键入：

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


## 启动Jupyter Notebook或者JupyterLab

通过常用终端启动：

```bash
jupyter lab
```

或者使用传统界面：

```bash
jupyter notebook
```


## Notebooks可视化

整个课程将使用*Jupyter Notebooks*进行交互式数据挖掘和可视化。

我们将使用*GitHub*和*Jupyter Notebook*的深色风格。建议你使用同样的风格，不然你的显示会不美观。JupyterLab有内建的深色主题可供选择，只有你希望在传统notebook界面下使用深色主题时需要额外安装主题。为了能够在传统notebook界面美观的查看课程内容，请参考以下内容：

 - [*Jupyter Notebook* 深色主题](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* 深色主题](https://userstyles.org/styles/37035/github-dark)，请注释掉 `invert #fff to #181818` 代码块.
