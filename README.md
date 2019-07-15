# Mini Course in Deep Learning with PyTorch for AIMS
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning-Minicourse/master)

The African Masters of Machine Intelligence (AMMI) is Africa's flagship program in machine intelligence led by The African Institute for Mathematical Sciences (AIMS).
These lessons, developed during the course of several years while I've been teaching at Purdue and NYU, are here proposed for the AMMI (AIMS).

Prior to this course delivered for AMMI (AIMS), an earlier version of this was delivered and video-recorded for the Computational and Data Science for High Energy Physics ([CoDaS-HEP](http://codas-hep.org/)) summer school at Princeton University.
Please refer to this version release [here](https://github.com/Atcold/pytorch-Deep-Learning-Minicourse/releases/tag/v1.0.0). 

## Table of contents
`T`: theory (slides and animations)  
`P`: practice (*Jupyter Notebooks*)

 1. `T` Learning paradigms: supervised-, unsupervised-, and reinforcement-learning
 2. `P` Getting started with the tools: Jupyter notebook, PyTorch tensors and autodifferentiation
 3. `T+P` Neural net's forward and backward propagation for classification and regression
 4. `T+P` Convolutional neural nets improve performance by exploiting data nature
 5. `T+P` Foundations of Salsa
 6. `T+P` Recurrent nets natively support sequential data
 7. `T+P` Unsupervised learning: vanilla and variational autoencoders, generative adversarial nets
 8. `T` How to create and deliver an effective presentation
 9. `T+P` Regularization for neural nets
 
## Sessions and relative material
 1. Time slot 1 (4h + 4h)  
    Topics: 1, 2, 3.  
    Slides: [01 - ML and spiral classification](slides/01%20-%20ML%20and%20spiral%20classification.pdf).  
    Notebooks: [01](01-tensor_tutorial.ipynb), [02](02-space_stretching.ipynb), [03](03-autograd_tutorial.ipynb), [04](04-spiral_classification.ipynb), [05](05-regression.ipynb).  
 2. Time slot 2 (4h + 2h)  
    Topic: 4.  
    Slides: [02 - CNN](slides/02%20-%20CNN.pdf).  
    Notebooks: [06](06-convnet.ipynb), [07](07-listening_to_kernels.ipynb).  
 3. Time slot 3 (2h)  
    Topic: 5.  
    Slides: [03 - Salsa](slides/03%20-%20Salsa.pdf).  
 4. Time slot 4 (4h + 4h)  
    Topic: 6.  
    Slides: [04 - RNN](slides/04%20-%20RNN.pdf).  
    Code Readings: [Word Language Model](https://github.com/pytorch/examples/blob/master/word_language_model/model.py).  
    Assignment: [HW1](assignments/hw1.pdf), [HW1 Solutions](assignments/hw1_solutions.pdf).  
    Notebooks: [08](08-seq_classification.ipynb), [09](09-echo_data.ipynb).  
 5. Time slot 5 (4h + 4h)  
    Topic: 7.  
    Slides: [05 - Generative models](slides/05%20-%20Generative%20models.pdf).  
    Code Readings: [GAN](https://github.com/pytorch/examples/blob/master/dcgan/main.py).  
    Guides: [TikZ Quick Guide](assignments/tikz_guide.pdf).  
    Notebooks: [10](10-autoencoder.ipynb), [11](11-VAE.ipynb).  
 6. Time slot 6 (1h)  
    Topic: 8.  
    Slides: [06 - How to present](slides/06%20-%20How%20to%20present.pdf).  
    Video: [How to prepare a presentation](https://youtu.be/y4N0_Tvt75s).  
 7. Time slot 7 (1h)  
    Topic: 9.  
    Slides: [07 - Regularisation](slides/07%20-%20Regularisation.pdf).    
    Assignment: [HW2](assignments/hw2.pdf).  
    Notebooks: [12](12-regularization.ipynb).  

## Notebooks visualisation
*Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.

We use dark styles for both *GitHub* and *Jupyter Notebook*.
You should try to do the same, or they will look ugly. JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface.
To see the content appropriately in the classic interface install the following:

 - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.

## Keeping in touch
Feel free to follow Afredo at [Twitter](https://twitter.com/alfcnz) and subscribe to his [YouTube channel](https://www.youtube.com/user/Atcold/) to have the latest free educational material.

For more educational materials you also can head to Ritchie's [website](https://www.ritchieng.com/).

# Getting started
To be able to follow the workshop exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
Following instruction would work as is for Mac or Ubuntu linux users, Windows users would need to install and work in the Gitbash terminal.

## Download and install Miniconda
Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.6 for your operating system.

```bash
wget <http:// link to miniconda>
sh <miniconda .sh>
```

After that, type:

```bash
conda --help
```

and read the manual.

## Check-out the git repository with the exercise
Once Miniconda is ready, checkout the course repository and and proceed with setting up the environment:

```bash
git clone https://github.com/Atcold/PyTorch-Deep-Learning-Minicourse
```

If you do not have git and do not wish to install it, just download the repository as zip, and unpack it:

```bash
wget https://github.com/Atcold/PyTorch-Deep-Learning-Minicourse/archive/master.zip
#For Mac users:
#curl -O https://github.com/Atcold/PyTorch-Deep-Learning-Minicourse/archive/master.zip
unzip master.zip
```

## Create isolated Miniconda environment
Change into the course folder, then type:

```bash
#cd PyTorch-Deep-Learning-Minicourse
conda env create -f environment.yml
source activate dl-minicourse
```

## Install Autocomplete by hinterland
You have to run the following commands if you want auto-complete.
```
pip install jupyter_contrib_nbextensions
pip install jupyter_nbextensions_configurator
jupyter contrib nbextension install --user

cd /usr/local/miniconda3/envs/dl-minicourse/lib/python3.6/site-packages/jupyter_contrib_nbextensions/nbextensions
jupyter nbextension install hinterland
jupyter nbextension enable hinterland/hinterland
```
## Start Jupyter notebook or JupyterLab
If you are working in a JupyterLab container double click on "Files" tab in the upper right corner.
Locate first notebook, double click to open.
Do not attempt to start `jupyter` from the terminal window.

If working on a laptop, start from terminal as usual:

```bash
jupyter lab
```

Or, for the classic interface:

```bash
jupyter notebook
```


## More PyTorch Resources
If you would like more PyTorch resources, head over to the global community-maintained repository of hundreds of reliable implementations and guides at the following repository created by Ritchie Ng: [The Incredible PyTorch](https://github.com/ritchieng/the-incredible-pytorch).
