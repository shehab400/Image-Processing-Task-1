import numpy as np
import matplotlib.pyplot as plt

# Constants
IMAGE_SIZE = 256
CHECKER_SIZE = 32

# Function to draw a checkerboard 
def generate_checkerboard(image_size, checker_size):
    im = np.zeros((image_size, image_size, 3))
    for i in range (0, image_size):
        for j in range (0, image_size):
            if (j//checker_size)%2 == 0:
                if (i//checker_size)%2 == 0:
                    im[i,j] = [0,0,0]
                else:
                    im[i,j] = [255,255,255]
            else:
                if (i//checker_size)%2 == 0:
                    im[i,j] = [255,255,255]
                else:
                    im[i,j] = [0,0,0]
    return im

# Function to calculate mean and standard deviation
def calculate_stats(image):
    return np.mean(image), np.std(image)

# Generate and plot the checkerboard
checkerboard = generate_checkerboard(IMAGE_SIZE, CHECKER_SIZE)
plt.imshow(checkerboard)
plt.title("Corrected Checkerboard")
plt.axis('off')
plt.show()

# Print statistics
mean, std = calculate_stats(checkerboard)
print(f"Mean: {mean:.2f}, Std Dev: {std:.2f}")


# Convert the checkerboard to grayscale because hist func is expecting only 2 values (0,1)
checkerboard_gray = np.mean(checkerboard, axis=2)

# Draw histogram
plt.hist(checkerboard_gray.ravel(), bins=256, range=(0, 256))
plt.title("Pixel Intensity Histogram")
plt.show()

# Warped checkerboard function (updated)
def warp_checkerboard(image):
    x = np.linspace(0, 2 * np.pi, IMAGE_SIZE)
    y = np.linspace(0, 2 * np.pi, IMAGE_SIZE)
    xx, yy = np.meshgrid(x, y)
    
    # Create warp displacement
    warp_x = (xx + 0.5 * np.sin(yy)) * (IMAGE_SIZE/(2*np.pi))
    warp_y = (yy + 0.5 * np.sin(xx)) * (IMAGE_SIZE/(2*np.pi))
    
    # Convert to integer coordinates
    warp_x = np.clip(warp_x, 0, IMAGE_SIZE-1).astype(int)
    warp_y = np.clip(warp_y, 0, IMAGE_SIZE-1).astype(int)
    
    return image[warp_x, warp_y]

# Generate and plot warped checkerboard
warped = warp_checkerboard(checkerboard)
plt.imshow(warped)
plt.title("Warped Checkerboard")
plt.axis('off')
plt.show()