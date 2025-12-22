from constants import *
from PIL import Image, ImageDraw
from math import floor

class Converter:
    def __init__(self, image_path:str):
        self.image = Image.open(image_path)
        self.image_width = self.image.width
        self.image_height = self.image.height
        self.strength_interval = TOTAL_RGB_VALUES / len(chars)    # Explained in the documentation.
    
    def scale_image(self) -> Image:
        resized_image = self.image.resize(size = (round(self.image_width * IMAGE_SCALOR),
                                            round(self.image_height * IMAGE_SCALOR)))
        return (resized_image)
    
    def determine_character(self, pixel_value:tuple) -> str:
        strength = sum(pixel_value) / len(pixel_value)
        index = floor(strength / self.strength_interval)
        return (chars[index])
    
    def _testing_determine_character(self, pixel_value:tuple) -> str:
        strength = sum(pixel_value) / len(pixel_value)
        index = floor(strength / self.strength_interval)
        return (index)
    
