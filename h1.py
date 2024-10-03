import matplotlib.pyplot as plt
import numpy as np

# Create a sample image
image = np.random.rand(10, 10)

def show_image(image, title='Sample Image', cmap_type='viridis'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Test with different color maps
show_image(image, cmap_type='plasma')
show_image(image, cmap_type='inferno')
show_image(image, cmap_type='magma')
show_image(image, cmap_type='cividis')


#The cmap parameter in Matplotlib’s imshow function allows you to specify different color maps for displaying images. 
# Here are a few popular options you can use:

#'viridis': A perceptually uniform color map.
#'plasma': A color map with a warm color scheme.
#'inferno': A color map with a dark-to-light color scheme.
#'magma': A color map with a black-to-white color scheme.
#'cividis': A color map designed for color vision deficiency.