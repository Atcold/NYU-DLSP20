---
title: Contribution instructions
lang-ref: about
---


Here you have some guidelines regarding your contribution, using markdown. If you're not yet familiar with this typesetting, have a look at [this cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Moreover, have a look at this markdown file in a proper text editor (say [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor))).


## (British) English

This website uses English spelling. So, there will be *colours*, *labelling*, *analogue*, *behaviour*, *modelled*, *maximum*, and so on.


## Adding figures

When adding figures, make sure they are centred in the page. To do this, follow this syntax:

```html
<center>
<img src="Network.png" style="zoom: 40%; background-color:#DCDCDC;" /><br>
<b>Figure 2:</b> Network architecture.
</center>
```

In this particular example, the author chose to resize the image to 40% of its original size. Given that the image had a transparent background, an additional light colour (`#DCDCDC`) has been added to the background. In this example, taken from `01-3.md`, the image is automatically fetched from the `/01-3/` directory, which is automatically prepended to the name of the image `Network.png`.


## Adding figures side by side

In this case the author displayed two figures, side by side, using a table.

```html
| <center><img src="Spiral1.png" width="200px"/></center> | <center><img src="Spiral2.png" height="170px"/></center> |
|            (a) Input points, pre-network                |           (b) Output points, post-network                |

<center><b>Figure 1:</b> Five color spiral.</center>
```

Moreover, since a specific size was needed, `width` or `height` can be specified.


## Adding headings

When adding headings, using two or three `#`, add an extra empty line in the source code.

```markdown
Some text from a preceding paragraph.
 - - 1 - -
 - - 2 - -
## New heading
 - - 1 - -
More text.
```


## Adding mathematical formula

This website uses [*KaTeX*](https://katex.org/), therefore you may want to check out what the [supported $\TeX$ functions are](https://katex.org/docs/supported.html). For inserting some in-line formula, enclose it in single dollar signs, for example `$y = mx + q \in \mathbb{R}$` renders as $ y = mx + q \in \mathbb{R}$. To insert a centred formula, you want to follow this syntax (pay attention to the empty lines).

```tex
Some text.
 - - 1 - -
$$
ax^2 + bx + c = 0 \quad\Rightarrow\quad
_1x_2 = {-b \pm \sqrt{b^2 - 4ac} \over 2a}
$$
 - - 1 - -
Some more text.
```

Some text.

$$
ax^2 + bx + c = 0 \quad\Rightarrow\quad
_1x_2 = {-b \pm \sqrt{b^2 - 4ac} \over 2a}
$$

Some more text.


## Mathematical notation

I am writing here a non exhaustive list of mathematical notation we're going to use for the class website. We are planning on adding macros to ease writing.

- The transposition symbol is `$^\top$`, which looks like $^\top$.
- Vectors should use a lower-case bold and italic typesetting. This can be done with `$\boldsymbol{x}$` and looks like $\boldsymbol{x}$. We may want to add a macro `\vect{}` for this.
- Matrices should use a upper-case bold and italic typesetting. This can be done with `$\boldsymbol{A}$` and looks like $\boldsymbol{A}$. We may want to add a macro `\matr{}` for this.
- Function names are **not** in italic, hence `$\max(\cdot)$`, `$\log(\cdot)$`, `$\tanh(\cdot)$`, which look like $\max(\cdot)$, $\log(\cdot)$, $\tanh(\cdot)$, and so on.
- The *exponential* function is `$\exp(\cdot)$`, $\exp(\cdot)$, and not `$e^{(\cdot)}$`, $e^{(\cdot)}$.
- Computer names use `$\texttt{}$` in the mathematical environment. For example we can write `$\texttt{ReLU}(\cdot)$` for $\texttt{ReLU}(\cdot)$. If we are just talking about computer stuff, then we shall write `ReLU` or `torch.relu()`. While writing formulas we should prefer using `$(\cdot)^+$`, $(\cdot)^+$, for the positive part.

