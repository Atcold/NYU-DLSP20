# Deep Learning with PyTorch [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning-Minicourse/master)
This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning-Minicourse/), where all the course mateiral can be found in video and textual format.

# Getting started
To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
The following instruction would work as is for Mac or Ubuntu linux users, Windows users would need to install and work in the Gitbash terminal.


## Download and install Miniconda
Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```

After that, type:

```bash
conda --help
```

and read the manual.


## Check-out the git repository with the exercise
Once Miniconda is ready, checkout the course repository and and proceed with setting up the environment:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning-Minicourse
```


## Create isolated Miniconda environment
Change directory (`cd`) into the course folder, then type:

```bash
# cd pytorch-Deep-Learning-Minicourse
conda env create -f environment.yml
source activate dl-minicourse
```

## Start Jupyter notebook or JupyterLab
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

