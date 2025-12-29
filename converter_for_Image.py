from constants import *
from PIL import Image, ImageDraw

characters_in_use = chars

class Converter_for_Image:
    def __init__(self, image_path:str):
        self.image = Image.open(image_path)
        self.image_width = self.image.width
        self.image_height = self.image.height
    
    def __del__(self):
        self.image.close()
        print("Converter_for_Image instance closed.")
    
    def _scale_image_for_ASCII(self) -> Image:
        resized_image = self.image.resize(size = (round(self.image_width * IMAGE_SCALOR / INDIVIDUAL_CHARACTER_WIDTH),
                                                    round(self.image_height * IMAGE_SCALOR / INDIVIDUAL_CHARACTER_HEIGHT)))
        return (resized_image)  # Every pixel is supposed to be a character!
    
    def _get_intensity_of_pixel_through_average(self, RGB:tuple) -> float:
        return (sum(RGB) / 3)
    
    def _get_intensity_of_pixel_though_weighted_average(self, RGB:tuple) -> float:
        return ((RED_WEIGHT * RGB[0]) + (GREEN_WEIGHT * RGB[1]) + (BLUE_WEIGHT * RGB[2]))
    
    def _get_character_index(self, intensity:float) -> int:
        return (round((intensity / MAX_RGB_VALUE) * (len(characters_in_use) - 1)))
    
    def convert_image_to_ASCII_through_average(self) -> str:
        scaled_image = self._scale_image_for_ASCII()
        rows_of_ASCII = []
        for y in range(scaled_image.height):
            current_row = []
            for x in range(scaled_image.width):
                pixel = scaled_image.getpixel(xy = (x, y))
                index = self._get_character_index(self._get_intensity_of_pixel_through_average(pixel))
                current_row.append(characters_in_use[index])
            rows_of_ASCII.append("".join(current_row))
        return ("\n".join(rows_of_ASCII))
    
    def draw_ASCII_image(self, ASCII:str) -> Image:
        rows = ASCII.split("\n")
        new_image_height = len(rows) * INDIVIDUAL_CHARACTER_HEIGHT
        new_image_width = len(rows[0]) * INDIVIDUAL_CHARACTER_WIDTH
        new_image = Image.new(mode = "RGB", size = (new_image_width, new_image_height), color = 0)
        drawing_object = ImageDraw.Draw(new_image)

        for y, row in enumerate(rows):
            for x, character in enumerate(row):
                position_to_draw = (x * INDIVIDUAL_CHARACTER_WIDTH, y * INDIVIDUAL_CHARACTER_HEIGHT)
                drawing_object.text(xy = position_to_draw, text = character)
        return (new_image)
