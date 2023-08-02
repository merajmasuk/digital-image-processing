import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots, but show no figure in the second index (1)
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# Show some content in the first subplot (0)
axs[0, 0].plot([1, 2, 3], [4, 5, 6])
axs[0, 0].set_title('Plot in Subplot (0)')

# Set the second subplot (1) to None to show no figure
axs[0, 1].axis('off')

# Show some content in the third subplot (2)
axs[1, 0].scatter([1, 2, 3], [4, 5, 6])
axs[1, 0].set_title('Scatter in Subplot (2)')

# Show some content in the fourth subplot (3)
axs[1, 1].bar([1, 2, 3], [4, 5, 6])
axs[1, 1].set_title('Bar in Subplot (3)')

plt.tight_layout()
plt.show()
