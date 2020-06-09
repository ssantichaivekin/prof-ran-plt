import plot_tools as plot

plot.line((0, 0), (0, 1), plot.RED, 1)
plot.line((1, 1), (2, 2), plot.BLUE, 2)

plot.dot((2, 2))
plot.dot((3, 3), col=plot.BLUE)

plot.text((3, 3), "my blue dot", plot.BLUE)

plot.show()
