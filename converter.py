from constants import *
from PIL import Image

class Converter:
    def __init__(self, image_path:str):
        self.image = Image.open(image_path)
        self.image_width = self.image.width
        self.image_height = self.image.height
    
    def scaled_image(self) -> Image:
        resized_image = self.image.resize(size = (round(self.image_width * IMAGE_SCALOR),
                                            round(self.image_height * IMAGE_SCALOR)))
        return (resized_image)
    
    
