import torch 
import random
import numpy as np
import torch.nn as nn
from torchvision.datasets import MNIST
import torchvision.transforms as transforms

# Device configuration
cuda = torch.cuda.is_available()
device = torch.device("cuda:0" if cuda else "cpu")
seed = 1008
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
if cuda:
  torch.cuda.manual_seed(seed)
  torch.cuda.manual_seed_all(seed)
  torch.backends.cudnn.benchmark = False
  torch.backends.cudnn.deterministic = True

import matplotlib.pyplot as plt

# Hyper-parameters
sequence_length = 28*2
input_size = 14
hidden_size = 128
num_layers = 2
num_classes = 10
batch_size = 100
num_epochs = 2
learning_rate = 0.01

def vis(model):
  # Loss
  criterion = nn.CrossEntropyLoss()

  for i, (images, labels) in enumerate(train_loader):
      images = images.reshape(-1, sequence_length, input_size).to(device).requires_grad_(True)
      labels = labels.to(device)
      
      # Forward pass
      outputs = model(images)
      loss = criterion(outputs, labels)
      loss.backward()
      break

def train_and_eval(model):
  # Loss and optimizer
  criterion = nn.CrossEntropyLoss()
  optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

  # Train the model
  model.train()
  total_step = len(train_loader)
  for epoch in range(num_epochs):
      for i, (images, labels) in enumerate(train_loader):
          images = images.reshape(-1, sequence_length, input_size).to(device)
          model.vis = False
          labels = labels.to(device)
          
          # Forward pass
          outputs = model(images)
          loss = criterion(outputs, labels)
          
          # # Backward and optimize
          optimizer.zero_grad()
          loss.backward()
          optimizer.step()

          
          if (i+1) % 100 == 0:
              print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
                    .format(epoch+1, num_epochs, i+1, total_step, loss.item()))
  # Test the model
  model.eval()
  with torch.no_grad():
      correct = 0
      total = 0
      for images, labels in test_loader:
          images = images.reshape(-1, sequence_length, input_size).to(device)
          labels = labels.to(device)
          outputs = model(images)
          _, predicted = torch.max(outputs.data, 1)
          total += labels.size(0)
          correct += (predicted == labels).sum().item()

      print('Test Accuracy of the model on the 10000 test images: {} %'.format(100 * correct / total)) 


def vis_weights(x):
  grads = []
  for i in x[0][:10]:
    a = i.mean() * 1e+16
    grads.append(a.cpu().item())
 
  plt.plot(grads)
  plt.show()

# MNIST dataset
train_dataset = MNIST(root='../../data/',
                                           train=True, 
                                           transform=transforms.ToTensor(),
                                           download=True)

test_dataset = MNIST(root='../../data/',
                                          train=False, 
                                          transform=transforms.ToTensor())

# Data loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size, 
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size, 
                                          shuffle=False)
