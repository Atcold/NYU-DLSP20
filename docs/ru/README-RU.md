<!-- # Deep Learning (with PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master) -->

# Глубокое обучение (с PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

<!-- This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format. -->

У данного репозитория с рабочими тетрадями сейчас есть [сопровождающий сайт](https://atcold.github.io/pytorch-Deep-Learning/ru), где Вы можете все материалы в текстовом и видео-формате.


<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese - Bengali - Hungarian -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md) &nbsp; [🇧🇩](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/bn/README-BN.md) &nbsp; [🇭🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/hu/README-HU.md)

<!-- # Getting started -->

# Начало работы

<!-- To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
The following instruction would work as is for Mac or Ubuntu Linux users, Windows users would need to install and work in the [Git BASH](https://gitforwindows.org/) terminal. -->

Чтобы иметь возможность выполнять упражнения, необходимо иметь ноутбук с предустановленной Miniconda (минимальная версия Anaconda) и несколько установленных Python пакетов.
Следующие инструкции будут работать, как для пользователей Mac, так и для Ubuntu Linux, Windows-пользователям желательно установить и работать в терминале [Git BASH](https://gitforwindows.org/).

<!-- ## Download and install Miniconda -->

## Загрузка и установка Miniconda

<!-- Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
``` -->

Пожалуйста, перейдите на [вебсайт Anaconda](https://conda.io/miniconda.html).
Скачайте и установите *the latest* версию Miniconda для *Python* 3.7 в соответствии с Вашей операционной системой.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```

<!-- ## Check-out the git repository with the exercise -->

## Изучите git-репозиторий с упражнениями

Как только Miniconda готова к работе, изучите репозиторий курса и продолжите работу с настройкой среды:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


<!-- ## Create isolated Miniconda environment -->

## Создайте изолированное окружение Miniconda

<!-- Change directory (`cd`) into the course folder, then type:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
``` -->

Смените директорию (`cd`) на папку курса, затем выполните в терминале:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


<!-- ## Start Jupyter Notebook or JupyterLab -->
## Запустите Jupyter Notebook или JupyterLab

<!-- Start from terminal as usual:

```bash
jupyter lab
```

Or, for the classic interface:

```bash
jupyter notebook
``` -->

Запустите из терминала, как обычно:

```bash
jupyter lab
```

Или для классического интерфейса:

```bash
jupyter notebook
```

<!-- ## Notebooks visualisation -->
## Визуализации рабочей тетради

<!-- *Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.

We use dark styles for both *GitHub* and *Jupyter Notebook*.
You should try to do the same, or they will look ugly.
JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface.
To see the content appropriately in the classic interface install the following: -->

*Jupyter Notebooks* используются на протяжении этих лекций для интерактивного исследования данных и визуализации.

Мы используем тёмные темы, как для *GitHub*, так и для *Jupyter Notebook*.
Вы должны попытаться проделать то же самое, или они будут выглядеть уродливо.
В JupyterLab есть встроенная тёмная тема, которую можно выбрать, то есть Вам нужно устанавливать что-то, если Вы хотите использовать классический интерфейс рабочей тетради.
Чтобы видеть контент соответствующим образом в классическом интерфейсе, установите следующее:

 - [тёмная тема *Jupyter Notebook*](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [тёмная тема *GitHub*](https://userstyles.org/styles/37035/github-dark) и закомментируйте блок кода `invert #fff to #181818`.
