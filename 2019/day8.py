import numpy as np
from PIL import Image

class LayeredImage():

    def __init__(self, image_data, image_height=6, image_width=25):
        self.image_data = image_data
        self.height     = image_height
        self.width      = image_width
        self.layer_size = image_height * image_width
        self.n_layers   = int(len(image_data) / self.layer_size)
        self.layers     = []
        self.__create_layers()

    def __create_layers(self):
        index = 0
        for _ in range(self.n_layers):
            layer = [[0 for x in range(self.width)] for y in range(self.height)] 
            for i in range(self.height):
                for j in range(self.width):
                    layer[i][j] = int(self.image_data[index])
                    index += 1
            self.layers.append(layer)

    def build_image(self):
        full_image = [[2 for x in range(self.width)] for y in range(self.height)] 

        for layer_idx in range(self.n_layers):
            layer = self.layers[layer_idx]
            for i in range(self.height):
                for j in range(self.width):
                    pixel_full  = full_image[i][j]
                    pixel_layer = layer[i][j]

                    if pixel_full == 2:
                        full_image[i][j] = pixel_layer
        return full_image

    def pixel_count(self):
        zeros = []
        ones = []
        twos = []

        for layer_idx in range(self.n_layers):
            layer = self.layers[layer_idx]
            zero = 0
            one = 0
            two = 0
            for i in range(self.height):
                for j in range(self.width):
                    pixel = layer[i][j]

                    if pixel == 0:
                        zero += 1

                    if pixel == 1:
                        one += 1

                    if pixel == 2:
                        two += 1

            zeros.append(zero)
            ones.append(one)
            twos.append(two)
        
        return zeros, ones, twos

import matplotlib.pyplot

layer_data = open('day8_input.txt').read().strip()
height = 6 
width = 25
image_builder = LayeredImage(layer_data, height, width)

# PART 1
zeros, ones, twos = image_builder.pixel_count()
index = zeros.index(min(zeros))
ans = ones[index] * twos[index]
print(ans)
# PART 2
image = image_builder.build_image()
image = np.array(image)
matplotlib.pyplot.imsave('message.png', image)


