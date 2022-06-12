<!-- Deep Learning (with PyTorch)
-->
# Aprendizaje Profundo (con PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

<!-- This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format.
-->
Este repositorio de *notebooks* tiene un [sitio web complementario](https://atcold.github.io/pytorch-Deep-Learning/es/), donde todo el material del curso puede ser encontrado en formato textual y de video.

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese - Bengali - Hungarian -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md) &nbsp; [🇧🇩](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/bn/README-BN.md) &nbsp; [🇭🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/hu/README-HU.md)

<!-- Getting started
-->
# Comenzando

<!-- To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
The following instruction would work as is for Mac or Ubuntu Linux users, Windows users would need to install and work in the [Git BASH](https://gitforwindows.org/) terminal.
-->
Para poder seguir los ejercicios, necesitarás un ordenador con Miniconda (una versión minimalista de Anaconda) y varios paquetes de Python instalados.
Las instrucciones siguientes funcionarán para los usuarios de Mac o Ubuntu Linux. Los usuarios de Windows necesitarán instalar y trabajar en una terminal [Git BASH](https://gitforwindows.org/).

<!-- Download and install Miniconda
-->
## Descarga e instala Miniconda

<!-- Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system.
-->
Ve al [sitio web de Anaconda](https://conda.io/miniconda.html).
Descarga e instala *la última* versión de Miniconda para *Python* 3.7 para tu sistema operativo.

<!-- wget <http:// link to miniconda>
-->
```bash
wget <http:// url a miniconda>
sh <miniconda*.sh>
```

<!-- Check-out the git repository with the exercise
-->
## Echa un vistazo al repositorio de git con los ejercicios

<!-- nce Miniconda is ready, checkout the course repository and proceed with setting up the environment:
-->
Una vez que Miniconda esté listo, revisa el repositorio del curso y continúa con la configuración del entorno:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```

<!-- Create isolated Miniconda environment
-->
## Crear un entorno aislado de Miniconda

<!-- Change directory (`cd`) into the course folder, then type:
-->
Cambia el directorio (`cd`) a la carpeta del curso, y luego escribe:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

<!-- Start Jupyter Notebook or JupyterLab
-->
## Inicia Jupyter Notebook o JupyterLab

<!-- Start from terminal as usual:
-->
Comienza desde la terminal como de costumbre:

```bash
jupyter lab
```

<!-- Or, for the classic interface:
-->
O, para la interfaz clásica:

```bash
jupyter notebook
```

<!-- Notebooks visualisation
-->
## Visualización de notebooks

<!-- *Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.
-->
Los *Cuadernos Jupyter* (Notebooks) se utilizan a lo largo de estas lecciones para la exploración y visualización interactiva de datos.

<!-- We use dark styles for both *GitHub* and *Jupyter Notebook*.
You should try to do the same, or they will look ugly.
JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface.
To see the content appropriately in the classic interface install the following:
-->
Utilizamos estilos oscuros para *GitHub* y *Jupyter Notebook*.
Deberías intentar hacer lo mismo, o se verán feos.
JupyterLab tiene incorporado un tema oscuro seleccionable, por lo que solo necesitarás instalar algunas cosas extras si deseas usar la interfaz clásica de las notebooks.
Para ver el contenido adecuadamente en la interfaz clásica, instala lo siguiente:

<!--  - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.
-->
 - [Tema oscuro para *Jupyter Notebook*](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [Tema oscuro para *GitHub*](https://userstyles.org/styles/37035/github-dark) y comenta el bloque de código `invert #fff to # 181818`.
