import matplotlib
# if your matplotlib doesn't pop up a window, force it to use tkinter backend
# matplotlib.use("tkagg")

from matplotlib import pyplot as plt

# Colors
# Define new colors as 4-tuples of the form (r, g, b, 1) where
# r, g, b are values between 0 and 1 indicating the amount of red, green, and blue.
RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
BLUE = (0, 0, 1, 1)

def line(ax, p1, p2, col=RED, linewidth=2):
    x0, y0 = p1
    x1, y1 = p2
    ax.plot([x0, x1], [y0, y1], color=col, linewidth=2)

def dot(ax, p, shape = 'o', col=RED):
    # For more dot shapes, see https://matplotlib.org/3.1.1/api/markers_api.html
    x, y = p
    ax.plot(x, y, 'o', color=col)

def text(ax, p, text, col=RED):
    # For more controls on text size, font, etc. see
    # https://matplotlib.org/3.1.0/api/text_api.html#matplotlib.text.Text
    x, y = p
    ax.text(x, y, text, color=col, fontsize=12)

def show():
    """ Display in matplotlib window. """
    plt.show()

def save(fig, file_name):
    """ Takes a string of the form filename.png as input and saves image to that file. """
    fig.savefig(file_name)

def setup():
    fig = plt.figure()
    ax = fig.subplots(1, 1) # creates a figure with one Axes (plot)
    ax.autoscale()
    ax.margins(0.1)
    ax.axis("off")
    return fig, ax