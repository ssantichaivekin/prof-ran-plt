import numpy as np

import matplotlib as mpl
# mpl.use('Agg')

from matplotlib import collections as mc
from matplotlib import pyplot as plt

# Colors
# Define new colors as 4-tuples of the form (r, g, b, 1) where
# r, g, b are values between 0 and 1 indicating the amount of red, green, and blue.
RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
BLUE = (0, 0, 1, 1)

# Initialize figure for drawing
fig = plt.figure()

def line(p1, p2, col=RED, linewidth=2):
    x0, y0 = p1
    x1, y1 = p2
    plt.plot([x0, x1], [y0, y1], color=col, linewidth=2)

def dot(p, shape = 'o', col=RED):
    # For more dot shapes, see https://matplotlib.org/3.1.1/api/markers_api.html
    x, y = p
    plt.plot(x, y, 'o', color=col)

def text(p, text, col=RED):
    # For more controls on text size, font, etc. see
    # https://matplotlib.org/3.1.0/api/text_api.html#matplotlib.text.Text
    x, y = p
    plt.text(x, y, text)

def show():
    """ Display in matplotlib window. """
    setup()
    plt.show()

def save(file_name):
    """ Takes a string of the form filename.png as input and saves image to that file. """
    setup()
    plt.savefig(file_name)

def setup():
    ax = plt.gca()
    ax.autoscale()
    ax.margins(0.1)
    plt.tight_layout()
    plt.axis('off')