import cv2
import math
import os

def create_tiles(img_name):
    img = cv2.imread("/Users/sucha/MohanLab/input-images/" + img_name)
    path = '/Users/sucha/MohanLab/output-images/'
    img_shape = img.shape

    tile_size = (int(0.33 * img_shape[0]), int(0.33 * img_shape[1]))
    offset = tile_size

    for i in range(int(math.ceil(img_shape[0] / (offset[1] * 1.0)))):
        for j in range(int(math.ceil(img_shape[1] / (offset[0] * 1.0)))):
            cropped_img = img[offset[1] * i:min(offset[1] * i + tile_size[1], img_shape[0]), offset[0] * j:min(offset[0] * j + tile_size[0], img_shape[1])]
            
            resized_img = cv2.resize(cropped_img, (int(cropped_img.shape[1] * 3), int(cropped_img.shape[0] * 3)))
            
            if resized_img.shape[0] == 768 and resized_img.shape[1] == 768:

                cv2.imwrite(os.path.join(path, "tile_" + str(i) + "_" + str(j) + "_" + img_name), resized_img)

images = os.listdir('/Users/sucha/input-images/')
for img_name in images:
    img_name = img_name.replace(" ", "")
    create_tiles(img_name)
