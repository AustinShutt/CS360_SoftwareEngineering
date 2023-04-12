import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt



def plot_image(img: np.array):
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray')
    
def plot_two_images(img1: np.array, img2: np.array):
    _, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(img1, cmap='gray')
    ax[1].imshow(img2, cmap='gray')

def calculate_target_size(img_size: int, kernel_size: int) -> int:
    num_pixels = 0
    
    # From 0 up to img size (if img size = 224, then up to 223)
    for i in range(img_size):
        # Add the kernel size (let's say 3) to the current i
        added = i + kernel_size
        # It must be lower than the image size
        if added <= img_size:
            # Increment if so
            num_pixels += 1
            
    return num_pixels

def convolve(img: np.array, kernel: np.array) -> np.array:
    # Assuming a rectangular image
    tgt_size = calculate_target_size(
        img_size=img.shape[0],
        kernel_size=kernel.shape[0]
    )
    # To simplify things
    k = kernel.shape[0]
    
    # 2D array of zeros
    convolved_img = np.zeros(shape=(tgt_size, tgt_size))
    
    # Iterate over the rows
    for i in range(tgt_size):
        # Iterate over the columns
        for j in range(tgt_size):
            # img[i, j] = individual pixel value
            # Get the current matrix
            mat = img[i:i+k, j:j+k]
            
            # Apply the convolution - element-wise multiplication and summation of the result
            # Store the result to i-th row and j-th column of our convolved_img array
            convolved_img[i, j] = np.sum(np.multiply(mat, kernel))
            
    return convolved_img

img = Image.open('word.png')
img = ImageOps.grayscale(img)
img = img.resize(size=(224, 224))

outline = np.array([ #mixture
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

outline2 = np.array([ #verticle lines
    [-.5,1,-.5],
    [-.5,1,-.5],
    [-.5,1,-.5]
])

outline3 = np.array([ #horizontal lines
    [-.5, -.5, -.5],
    [1, 1, 1],
    [-.5, -.5, -.5]
])

img_outlined = convolve(img=np.array(img), kernel=outline)
for i in range(1):
    img_outlined = convolve(img=np.array(img_outlined), kernel=outline)


plot_two_images(
    img1=img, 
    img2=img_outlined
)
plt.show()
plt.pause(0.001)
#input("Press [enter] to continue.")