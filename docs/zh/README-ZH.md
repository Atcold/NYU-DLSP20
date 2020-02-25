# 深度学习 (使用PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)


**EN:** This repo hosts the Mandarin translation of the [companion website](https://atcold.github.io/pytorch-Deep-Learning/) of [Deep Learning (with PyTorch)](https://github.com/Atcold/pytorch-Deep-Learning) Jupyter Notebook repo and its `README.md`.

这份笔记的仓库具有[同步网站](https://atcold.github.io/pytorch-Deep-Learning/)，在那里您可以获得所有课程资料的视频与文本.


# 起步

为了能够完成练习，你需要为你的电脑安装Miniconda (Anaconda的精简版本)和一些Python包。以下说明步骤适用于Mac或者Ubuntu Linux用户，Windows用户需要安装[Git BASH](https://gitforwindows.org/)终端，并在该终端中完成操作。



## 下载并安装Miniconda

请前往[Anaconda网站](https://conda.io/miniconda.html)，下载并且安装适合你的操作系统的*最新*
Miniconda版本。其中*Python*版本请选择3.7


```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```

## 签出带有练习的git仓库

一旦你的Miniconda准备妥当，请签出课程的git仓库，同时建立Miniconda环境。

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```

## 创建独立的Miniconda环境

进入(`cd`)课程目录， 然后键入：

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

## 启动Jupyter Notebook或者JupyterLab

通过终端正常启动：

```bash
jupyter lab
```

或者采用传统界面：

```bash
jupyter notebook
```

## Notebooks可视化

整个课程将使用*Jupyter Notebooks*进行数据探索和可视化。


我们将使用*GitHub* 和 *Jupyter Notebook*的深色风格。建议你使用同样的风格，不然你的显示会不美观。JupyterLab具有内建的可选择的深色主题，因此，如果你希望在传统notebook界面下使用深色主题，只需要进行简单安装即可。为了能够在传统notebook界面，美观的查看课程内容，请参考以下安装：

 - [*Jupyter Notebook* 深色主题](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* 深色主题](https://userstyles.org/styles/37035/github-dark)，请注释掉 `invert #fff to #181818` 代码块.

