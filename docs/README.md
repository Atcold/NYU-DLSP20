# Website generation

[This repo's website](https://atcold.github.io/pytorch-Deep-Learning) is automatically served via [GitHub Pages](https://pages.github.com/) using [Jekyll](https://jekyllrb.com/).

# Running locally

## Clone the Repo

First, you need to clone this repo with all submodules. You need to do:

```bash
git clone --recursive <repo>
```

If you have already cloned it, you can simply do:

```bash
git submodule update --init --recursive
```

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

## Adding a chapter or section

If you need to add one more chapter or section, you will need to edit the `_config.yml` file in order to make it aware of your new contribution. More specifically you will need to add one or more line to the website outline, which looks like this at the moment.

```yaml
chapters:
  - path: chapters/01.md
    sections:
      - path: chapters/01-1.md
      - path: chapters/01-2.md
      - path: chapters/01-3.md
  - path: chapters/02.md
    sections:
      - path: chapters/02-1.md
      - path: chapters/02-2.md
      - path: chapters/02-3.md
```

The images for a given `section` will be fetched from a folder having the same name of the `section`'s file name, without considering the file extension. So, images for the file `02-2.md` will be automatically retrieved from the `02-2\` directory. The file will not be rendered well here in the repo, but `jekyll` will do a good job on the besite.