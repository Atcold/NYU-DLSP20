https://ml-front.nautilus.optiputer.net/

# PyTorch-Deep-Learning-Minicourse
Minicourse in Deep Learning with PyTorch

## Table of contents
`T`: theory
`P`: practice

 1. `T` Learning paradigms: supervised-, unsupervised-, and reinforcement-learning
 2. `P` Getting started with the tools: Jupyter notebook, PyTorch tensors and autodifferentiation
 3. `T+P` Neural net's forward and backward propagation for classification
 4. `T+P` Convolutional neural nets improve performance by exploiting data nature
 5. `T+P` Recurrent nets natively support sequential data
 6. `T+P` Unsupervised learning: vanilla and variational autoencoders, generative adversarial nets
 7. `T+P` Fighting overfitting: regularisation and other techniques

## Sessions
 1. Time slot 1 (1h30min + 45 min = 2h15min) on Tuesday afternoon (1, 2, 3)
 2. Time slot 2 (1h30min + 45 min = 2h15min) on Wednesday afternoon (4)
 3. Extra section (45min) on Thursday afternoon
 4. Extra section (1h30min) on Friday morning

## Notebooks visualisation
*Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.

I use dark styles for both *GitHub* and *Jupyter Notebook*.
You better do the same, or they will look ugly.
To see the content appropriately install the following:

 - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.

# Getting started
To be able to follow the workshop exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed. Following instruction would work as is for Mac or Ubuntu linux users, Windows users would need to install and work in the Gitbash terminal.

## Download and install Miniconda
Please go to the following website: https://conda.io/miniconda.html
download and install *the latest* Miniconda version for Python 3.6 for your operating system. 
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
Once Miniconda is ready, checkout the course repository and
and proceed with setting up the environment:

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
conda env create -f conda-envt.yml
source activate codas-ml
```

## Enable anaconda kernel in Jupyter

To make newly created miniconda environment visible in the Jupyter, install `ipykernel`:

```bash
python -m ipykernel install --user --name codas-ml --display-name "Codas ML"
```

## Start jupyter notebook

If you are working in a JupyterLab container double click on "Files" tab in the upper right corner. Locate first notebook, double click to open. Do not attempt to start `jupyter` from the terminal window.


If working on a laptop, start from terminal as usual:
```bash
jupyter notebook
```
