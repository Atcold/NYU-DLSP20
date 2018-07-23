# matplotlib and stuff
import matplotlib.pyplot as plt
import numpy as np


def plt_style(c='k'):
    """
    Set plotting style for bright (``c = 'w'``) or dark (``c = 'k'``) backgrounds

    :param c: colour, can be set to ``'w'`` or ``'k'`` (which is the default)
    :type c: str
    """
    import matplotlib as mpl
    from matplotlib import rc

    # Reset previous configuration
    mpl.rcParams.update(mpl.rcParamsDefault)
    # %matplotlib inline  # not from script
    get_ipython().run_line_magic('matplotlib', 'inline')

    # configuration for bright background
    if c == 'w':
        plt.style.use('bmh')

    # configurations for dark background
    if c == 'k':
        plt.style.use(['dark_background', 'bmh'])

    # remove background colour, set figure size
    rc('figure', figsize=(16, 8), max_open_warning=False)
    rc('axes', facecolor='none')


def plt_interactive(c='k'):
    from matplotlib import rc
    import matplotlib as mpl
    mpl.rcParams.update(mpl.rcParamsDefault)
    get_ipython().run_line_magic('matplotlib', 'notebook')
    plt.rc('figure', figsize=(9.5, 4.75), facecolor=c)
    # configuration for bright background
    if c == 'w':
        plt.style.use('bmh')

    # configurations for dark background
    if c == 'k':
        plt.style.use(['dark_background', 'bmh'])
    rc('axes', facecolor='none')

plt_style()
