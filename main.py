from converter import Converter_for_Image
from constants import *

# Standard
image_path = "Andromeda_Galaxy.jpeg"
converter = Converter_for_Image(image_path)

product = converter.convert_image_to_ASCII_through_average()
with open("product.txt", "w") as file:
    file.write(product)
image_product = converter.draw_ASCII_image(product)
image_product.save("product.png")