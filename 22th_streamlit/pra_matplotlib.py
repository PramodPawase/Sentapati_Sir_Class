import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a simple line plot
plt.plot(x, y, color='blue', marker='o', linestyle='--')

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot Example")

# Show the plot
plt.show()
