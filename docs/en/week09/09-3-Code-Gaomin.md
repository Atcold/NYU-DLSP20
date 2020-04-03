## Difference between GAN (Generative Adversarial Network) and VAE (Variational Autoencoder)

![](/images/week09/09-3/GANvsVAE.jpg)

Let's recall from the notes of Week 8, a VAE (on the left part of the figure) use an encoder to map the input $x$ from input space to latent space, adding some noise. Next, it decodes from latent space to output space. In VAE, we have reconstruction loss to messure the distance between the input and output. And of course, we try to minimize the loss, as we want the output $\hat x $ and the input $x$ to be close.

For GAN, we start from the sampler (similar to the latent space in VAE), and use a generative network to map $z$  in the latent space into $\hat x$ in the input space. The main difference from VAE is, in GAN **we do not measure a direct relationship (i.e, reconstruction loss) between the output of the generative network $\hat x$ and the real data $x$.** Instead we train a discriminator/ cost network which would give the real data $x$ a low cost, and a generator output/ the fake data $\hat x$ a high cost.



## Major Pitfalls in GANs

### 1. Unstable Convergence

As the generator improves with training, the discriminator performance gets worse because the discriminator can't easily tell the difference between real and fake. If the generator succeeds perfectly, then the discriminator has many misclassifications. So whenever a generator works, the disciminator fails.

This progression poses a problem for convergence of the GAN as a whole: the discriminator feedback gets less meaningful over time. If the GAN continues training past the point when the discriminator is giving completely random feedback, then the generator starts to train on junk feedback, and its own quality may collapse. [Refer to [training convergence in GANs](https://developers.google.com/machine-learning/gan/training)]

There is no convergence, but there is a unstable equilibrium point, which is very tricky to catch.

###  2. Vanishing Gradient

Let's consider we are using the binary cross entropy loss for the discriminator

$$L = - E_x[log(D(x))] - E_\hat x[log(1-D(\hat x))]$$. 

When the discriminator is perfect, we are guaranteed with $D(x)=1$ and $D(\hat x)=0$, where $D(z)$ denote the output of the discriminator/ cost network given input $z$. Therefore the loss function falls to zero and we end up with no gradient to update the loss during learning iterations for both discriminator network and generative network. Thus, when training a GAN, you want to make sure that the cost gradually increases as you move away the true data.

### 3. Mode Collapse

 If a generator always map the every input from sampler into a *single* $\hat x$, and it's a plausible $\hat x$ that can fool the discriminator. Then the generator can produce *only* that output. A possible solution to this issue is to enfore some penalty to the generator for always giving the same output given different inputs.



### Question:

In general, any ways to make sure the GANs converge into the right point?

Answer:

A way that people usually do is to train several GANs and evaluate it through some metric, and compare it with the metric on the training data. A metric is Inception Score (IS), which can be messure by a training an inception network.

