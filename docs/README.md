# Website generation

[This repo's website](https://atcold.github.io/pytorch-Deep-Learning-Minicourse/) is automatically served via [GitHub Pages](https://pages.github.com/) using [Jekyll](https://jekyllrb.com/).

# Running locally

## Installation

If you want to debug it locally, you need to install `jekyll`, starting by installing `gem` and exporting it's `PATH`.

```bash
brew install ruby
export PATH=/usr/local/opt/ruby/bin:$PATH
gem install jekyll
```

To figure out where `jekyll` has been installed, we can query `gem`:

```bash
gem environment gemdir
```

which for me is `/usr/local/lib/ruby/gems/2.6.0`.

## Serve locally

Given that we know where to find `jekyll`, we can serve the website with the following command:

```bash
/usr/local/lib/ruby/gems/2.6.0/bin/jekyll serve --trace --baseurl ''
```

For your convenience there's an execturable in this directory containing this exact line. So, all you need to do to run the web server is typing:

```bash
./serve.sh
```

