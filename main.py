import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a sample dataset with three dimensions (x, y, z)
data = [
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 5),
    # Add more data points as needed
]

# Unpack the data into separate lists for each dimension
x, y, z = zip(*data)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

# Set labels for each axis
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()
