from converter import Converter
from constants import *

# Standard
image_path = "Andromeda_Galaxy.jpeg"
converter = Converter(image_path)

intensity = converter.get_intensity_of_pixel_through_average((0, 0, 0))
index = converter.get_character_index(intensity)
print(index)

print(simpler_chars[index])