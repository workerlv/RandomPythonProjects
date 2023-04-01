import cv2 # pip install opencv-python
import os


def calculate_size(scale_perc, width, height):
    # scale_perc - how much % of original image size should be new image size
    new_width = int(width * scale_perc / 100)
    new_height = int(height * scale_perc / 100)
    return new_width, new_height


def resize(image_path, scale_perc, resized_path):
    image = cv2.imread(image_path)
    new_dim = calculate_size(scale_perc, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_image)


# get all images_to_resize from folder and resize them
all_images = os.listdir("images_to_resize")
for img in all_images:
    resize(f"images_to_resize/{img}", 30, f"resized_images/{img}")
