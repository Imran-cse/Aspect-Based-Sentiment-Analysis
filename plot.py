import matplotlib.pyplot as plt
import numpy as np


# function for plotting graph
def plot_axes():
    # initialize graph
    ax = plt.subplot(1, 1, 1)

    # scale the axes
    ax.set_xticks(np.arange(-10, 11, 1))
    ax.set_yticks(np.arange(-10, 11, 1))

    # display grid lines
    ax.grid(True)

    # shift the axes to center
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # display the plotting
    plt.show()


# function for plotting base object
def plot_points(x, y, lineColor, pointColor):
    # initialize graph
    ax = plt.subplot(1, 1, 1)

    # plot in the graph
    ax.plot(x, y, lineColor, x, y, pointColor)
    #ax.plot(x2, y2, lineColor2, x2, y2, pointColor2)

    # scale the axes
    ax.set_xticks(np.arange(-6, 6.25, 0.25))
    ax.set_yticks(np.arange(-1, 1.25, 0.25))

    # display grid lines
    ax.grid(True)

    # shift the axes to center
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # display the plotting
    plt.show()

def plot_window(x, y, lineColor, pointColor):

    # initialize graph
    ax = plt.subplot(1, 1, 1)

    # plot in the graph
    ax.plot(x, y, lineColor, x, y, pointColor)

    # scale the axes
    ax.set_xticks(np.arange(-10, 11, 1))
    ax.set_yticks(np.arange(-10, 11, 1))

    # display grid lines
    ax.grid(True)

    # shift the axes to center
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # display the plotting
    plt.show()

def plot_show():
    # display the plotting
    plt.show()

def plot_figure(k):
    # display the plotting
    plt.figure(k)

