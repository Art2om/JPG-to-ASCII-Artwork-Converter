from converter_for_Image import Converter_for_Image
from converter_for_Video import Converter_for_Video
from constants import *

# Standard
image_path = "Andromeda_Galaxy.jpeg"
video_path = "Rotating_Cube.mp4"
frame_folder = "frame_folder"
ASCII_folder = "ASCII_frame_folder"
converter_image = Converter_for_Image(image_path)
converter_video = Converter_for_Video(video_path)

'''
product = converter_image.convert_image_to_ASCII_through_average()
with open("product.txt", "w") as file:
    file.write(product)
image_product = converter_image.draw_ASCII_image(product)
image_product.save("product.png")
'''

converter_video.convert_video_to_ASCII_video(frame_folder, ASCII_folder)

# Standard
del converter_image
del converter_video