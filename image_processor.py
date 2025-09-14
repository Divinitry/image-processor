from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("test_images/heatmaptest.jpg")
greyscale_averages = (255, 204, 153, 102, 51, 0)

# specify the grid size the determine how big the pixels will be (1x1 2x2 3x3 4x4 etc..) 
grid_size = 1 

def find_greyscale(pixel_rgb_average):
    closest_rgb = min(greyscale_averages, key=lambda x: abs(x - pixel_rgb_average))
    greyscale_rgb = (closest_rgb, closest_rgb, closest_rgb)
    return greyscale_rgb

def rgb_normalizer(rgb_value):
    rgb_sum = 0
    for rgb_tuple in rgb_value:
        rgb_sum += sum(rgb_tuple)
    normalized_rgb = rgb_sum // (len(rgb_value) * 3)
    return find_greyscale(normalized_rgb)

image_array = np.array(im)
im_width = image_array.shape[1]
im_height = image_array.shape[0]

for y in range(0, im_height, grid_size):
    for x in range(0, im_width, grid_size):
        rgb_pixel_group = []
        for grid_y in range(grid_size):
            for grid_x in range(grid_size):
                x_value = min(x + grid_x, im_width - 1)
                y_value = min(y + grid_y, im_height - 1)
                current_pixel = im.getpixel((x_value, y_value))
                rgb_pixel_group.append(current_pixel)
        
        normalized_rgb = rgb_normalizer(rgb_pixel_group)
        
        for grid_y in range(grid_size):
            for grid_x in range(grid_size):
                x_value = min(x + grid_x, im_width - 1)
                y_value = min(y + grid_y, im_height - 1)
                image_array[y_value, x_value] = normalized_rgb

updated_image = Image.fromarray(image_array.astype('uint8'))


plt.imshow(updated_image)
plt.axis('off')
plt.show() 