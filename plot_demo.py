import plot_tools

fig = plot_tools.FigureWrapper("Example Plot")
fig.line((1, 1), (2, 2), col=plot_tools.RED)
fig.dot((2, 2), col=plot_tools.BLUE)
fig.text((3, 3), "my blue dot", col=plot_tools.BLUE)
fig.show()
