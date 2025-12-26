from constants import *
from PIL import Image, ImageDraw
from math import floor

class Converter:
    def __init__(self, image_path:str):
        self.image = Image.open(image_path)
        self.image_width = self.image.width
        self.image_height = self.image.height
    
    def scale_image(self) -> Image:
        resized_image = self.image.resize(size = (round(self.image_width * IMAGE_SCALOR),
                                            round(self.image_height * IMAGE_SCALOR)))
        return (resized_image)
    
    def get_intensity_of_pixel_through_average(self, RGB:tuple) -> float:
        return (sum(RGB) / 3)
    
    def get_intensity_of_pixel_though_weighted_average(self, RGB:tuple) -> float:
        return ((RED_WEIGHT * RGB[0]) + (GREEN_WEIGHT * RGB[1]) + (BLUE_WEIGHT * RGB[2]))
    
    def get_character_index(self, intensity:float) -> int:
        return (round((intensity / MAX_RGB_VALUE) * (len(simpler_chars) - 1)))
    
