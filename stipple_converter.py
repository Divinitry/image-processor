from PIL import Image
import numpy as np
import matplotlib as plt

'''
basic concept is that we take in an image and we conver that image to dots, we stipple the image with dots in black white and grey color scale
steps: 
1. set up the ability to take in user image 
2. process said image, convert to pixels, loop over each one, get average colours so u can balance the colours - pillow does this well, we load in the image and then loop over each pixel
3. find intensity of each pixel and replace it with a dot of equal intensity colour - average of rgb value 
4. output final product with matplotlib and then ask if the user wants to save it and then we can convert it to png and export it - use .save() from pillow to do this
5. final set up a website to do this and have this as the backend. 
'''

