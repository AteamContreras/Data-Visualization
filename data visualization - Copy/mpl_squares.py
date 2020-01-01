import matplotlib.pyplot as plt


# The numbers used in the graph.
squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]

# Style of Graph   ('seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight', 'seaborn')
plt.style.use('seaborn-dark')

# What you want to plot on the graph.
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title, and label axis.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis= 'both', labelsize=14)

# Shows the graph (run). 
plt.show()