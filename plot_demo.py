import plot_tools

fig, ax = plot_tools.setup()
plot_tools.line(ax, (1, 1), (2, 2), col=plot_tools.RED)

plot_tools.dot(ax, (2, 2), col=plot_tools.BLUE)

plot_tools.text(ax, (3, 3), "my blue dot", col=plot_tools.BLUE)

plot_tools.show()
