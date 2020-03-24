# Aprendizaje Profundo (con PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)


Este repositorio de *notebooks* tiene un [sitio web complementario](https://atcold.github.io/pytorch-Deep-Learning/), donde todo el material del curso puede ser encontrado en formato textual y de video.


# Comenzando

Para poder seguir los ejercicios, necesitarás un ordenador con Miniconda (una versión minimalista de Anaconda) y varios paquetes de Python instalados.
Las instrucciones siguientes funcionarán para los usuarios de Mac o Ubuntu Linux, los usuarios de Windows necesitarían instalar y trabajar en una terminal [Git BASH](https://gitforwindows.org/).


## Descarga e instala Miniconda

Ve al [sitio web de Anaconda](https://conda.io/miniconda.html).
Descarga e instala *la última* versión de Miniconda para *Python* 3.7 para tu sistema operativo.

```bash
wget <http:// url a miniconda>
sh <miniconda*.sh>
```


## Echa un vistazo al repositorio de git con los ejercicios

Una vez que Miniconda esté listo, revisa el repositorio del curso y continúa con la configuración del entorno:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


## Crear un entorno aislado de Miniconda

Cambia el directorio (`cd`) a la carpeta del curso, y luego escribe:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


## Inicia Jupyter Notebook o JupyterLab

Comienza desde la terminal como de costumbre:

```bash
jupyter lab
```

O, para la interfaz clásica:

```bash
jupyter notebook
```


## Visualización de notebooks

Los *cuadernos Jupyter* (notebooks) se utilizan a lo largo de estas clases para la exploración y visualización interactiva de datos.

Utilizamos estilos oscuros para *GitHub* y *Jupyter Notebook*.
Deberías intentar hacer lo mismo, o se verán feos.
JupyterLab tiene incorporado un tema oscuro seleccionable, por lo que solo necesitas instalar algo extra si deseas usar la interfaz clásica de las notebooks.
Para ver el contenido adecuadamente en la interfaz clásica, instala lo siguiente:

 - [Tema oscuro para *Jupyter Notebook*] (https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [Tema oscuro para *GitHub*] (https://userstyles.org/styles/37035/github-dark) y comenta el bloque de código `invert #fff to # 181818`.