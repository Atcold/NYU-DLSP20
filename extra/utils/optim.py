from torch.optim import Optimizer
import math
import torch
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt


class Optim(Optimizer):
   
    def __init__(self, params, defaults):
        super(Optim, self).__init__(params, defaults)

    def step(self, closure=None):
        """Performs a single optimization step.

        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue
                self.my_step(p, self.state[p], group)
        return loss
    
    def my_step(self, p, state, group):
      raise NotImplementedError

plt.ioff() #(interactive mode)

A = torch.tensor([[1.0, 0.0,], [0.0, 5.0]])
b = torch.tensor([0.0, 0.0])

def objective(x, y):
    xy = torch.tensor([x, y])
    return (0.5 * xy @ (A @ xy) + b @ xy).item()

delta = 0.025
x = np.arange(-0.5, 1.5, delta)
y = np.arange(-8, 1.8, delta)
X, Y = np.meshgrid(x, y)
Z = np.copy(X)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = objective(X[i,j], Y[i,j])

w = torch.tensor([1.0, 1.0])
w.requires_grad_()

def output(opt, nsteps = 10, noise=0.0, fname="example.png"):
    torch.manual_seed(42)
    w.data[0] = 1.0
    w.data[1] = 1.0

    xopt = []
    yopt = []

    for i in range(nsteps):
        xopt.append(w[0].item())
        yopt.append(w[1].item())

        def obj():
            if noise > 0.0:
                bnoise = torch.normal(b, noise)
            else:
                bnoise = b
            loss = 0.5 * w @ (A @ w) + bnoise @ w
            opt.zero_grad()
            loss.backward()
            return loss

        opt.step(closure=obj)

    fig, ax = plt.subplots(figsize=(3,6))
    plt.axis('equal')
    CS = ax.contour(X, Y, Z, levels=[0.01 , 0.05, 0.1, 0.5, 1, 2, 3, 4, 5, 6])
    ax.clabel(CS, fontsize=7)

    ax.plot(0, 0, '.', color='blue')
    ax.plot(xopt, yopt, '-', color='red')
    ax.plot(xopt, yopt, '.', color='black')
    plt.ylim([-1.5, 1.5])
    plt.xlim([-0.6, 1.1])

    # fig.savefig(fname, bbox_inches='tight', pad_inches=0)
    fig.canvas.draw()
    plt.show()

