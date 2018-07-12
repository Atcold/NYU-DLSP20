# PyTorch-Deep-Learning-Minicourse
Minicourse in Deep Learning with PyTorch

## Table of contents
`T`: theory
`P`: practice

 1. `T` Learning paradigms: supervised-, unsupervised-, and reinforcement-learning
 2. `P` Getting started with the tools: Jupyter notebook, PyTorch tensors and autodifferentiation
 3. `T+P` Supervised learning: regression and classification
 4. `T+P` Neural net's forward and backward propagation
 5. `T+P` Convolutional, spectral, recurrent, and graph neural nets improve performance by exploiting data nature
 6. `T+P` Unsupervised learning: vanilla and variational autoencoders, generative adversarial nets

# Getting started

To be able to follow the workshop exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed. Following instruction would work as is for Mac or Ubuntu linux users, Windows users would need to install and work in the Gitbash terminal.

## Download and install Miniconda

Please go to the following website: https://conda.io/miniconda.html
download and install *the latest* Miniconda version for Python 3.6 for your operating system. 

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
