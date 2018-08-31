# PyTorch-Deep-Learning-Minicourse
Minicourse in Deep Learning with PyTorch [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Atcold/PyTorch-Deep-Learning-Minicourse/master)

These lessons, developed during the course of several years while I've been teaching at Purdue and NYU, are here proposed for the Computational and Data Science for High Energy Physics ([CoDaS-HEP](http://codas-hep.org/)) summer school at Princeton University.
The whole course has been recorded and the playlist is made available [here](https://youtu.be/S2kNR3R30s8).
Check the slides for drawings of better visual quality.
I'm also planning to record them in a more quiet environment and at a slower pace, add them to my YouTube channel, and made available [here](https://github.com/Atcold/pytorch-Video-Tutorials).

## Table of contents
`T`: theory (slides and animations)  
`P`: practice (*Jupyter Notebooks*)

 1. `T` Learning paradigms: supervised-, unsupervised-, and reinforcement-learning
 2. `P` Getting started with the tools: Jupyter notebook, PyTorch tensors and autodifferentiation
 3. `T+P` Neural net's forward and backward propagation for classification
 4. `T+P` Convolutional neural nets improve performance by exploiting data nature
 5. `T+P` Unsupervised learning: vanilla and variational autoencoders, generative adversarial nets
 6. `T+P` Recurrent nets natively support sequential data

## Sessions and relative material
 1. Time slot 1 (1h30min + 45 min = 2h15min) on Tuesday afternoon  
    Topics: 1, 2, 3.  
    Slides: [01 - ML and spiral classification](slides/01%20-%20ML%20and%20spiral%20classification.pdf).  
    Notebooks: [01](01-tensor_tutorial.ipynb), [02](02-space_stretching.ipynb), [03](03-autograd_tutorial.ipynb), [04](04-spiral_classification.ipynb).  
    Video: [01](https://youtu.be/u--4YzUQlj8), [02](https://youtu.be/panJ-pkaqBQ).
 2. Time slot 2 (1h30min + 45 min = 2h15min) on Wednesday afternoon  
    Topics: 4.  
    Slides: [02 - CNN](slides/02%20-%20CNN.pdf).  
    Notebooks: [05](05-convnet.ipynb).  
    Video: [03](https://youtu.be/jFK4odq_f0A), [04](https://youtu.be/ST73HFC4Lpo).
 3. Extra section (45min) on Thursday afternoon  
    Topics: 5.  
    Slides: [03 - Generative models](slides/03%20-%20Generative%20models.pdf).  
    Notebooks: [06](06-autoencoder.ipynb), [07](07-VAE.ipynb).  
    Video: [05](https://youtu.be/PRKq8ztYkZw).
 4. Extra section (1h30min) on Friday morning  
    Topics: 6.  
    Slides: [04 - RNN](slides/04%20-%20RNN.pdf).  
    Notebooks: [08-1](08-1-classify_seq_data.ipynb), [08-2](08-2-echo_data.ipynb), [08-3](08-3-temporal_order_classification_experiments.ipynb), [08-4](08-4-echo_experiments.ipynb	).  
    Video: [06](https://youtu.be/S2kNR3R30s8).

## Notebooks visualisation
*Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.

I use dark styles for both *GitHub* and *Jupyter Notebook*.
You better do the same, or they will look ugly.
To see the content appropriately install the following:

 - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.

## Media coverage
 - Princeton Research Computing [article](https://researchcomputing.princeton.edu/news/princetons-codas-hep-summer-school-young-physicists-gain-edge-computational-skills);
 - Princeton University main page [article](https://www.princeton.edu/news/2018/07/27/princeton-summer-program-graduate-student-physicists-gain-computational-skills).

## Keeping in touch
Feel free to follow me on [Twitter](https://twitter.com/AlfredoCanziani) and subscribe to my [YouTube channel](https://www.youtube.com/user/Atcold/) to have the latest free educational material.

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
source activate codas-ml
```

## Enable anaconda kernel in Jupyter
To make newly created miniconda environment visible in the Jupyter, install `ipykernel`:

```bash
python -m ipykernel install --user --name codas-ml --display-name "Codas ML"
```

## Start jupyter notebook
If you are working in a JupyterLab container double click on "Files" tab in the upper right corner.
Locate first notebook, double click to open.
Do not attempt to start `jupyter` from the terminal window.

If working on a laptop, start from terminal as usual:

```bash
jupyter notebook
```
