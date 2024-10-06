# Title : JPG to ASCII Artwork Converter
# Author : Artyom Svetlichnyy (following a tutorial from "Raphson" on Youtube)
# Date: October, 2024

# Libraries:
from PIL import Image, ImageDraw, ImageFont
import math

# Constant(s):
MAX_RGB_VALUE = 256
SIGNLE_CHAR_HEIGHT = 18
SIGNLE_CHAR_WIDTH = 8
SCALE_FACTOR = 0.4
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^'. "[: : (-1)]
# Below is a simplified set of characters.
#chars = "#@Wo-/\\ "[: : (-1)]

# Loads the image, (print statements are for debugging image size.)
im = Image.open("_____________________________.jpg")
width, height = im.size
print(width, height)
# Resizing the image by the <<SCALE FACTOR>>.
im = im.resize((int(SCALE_FACTOR * width), int(SCALE_FACTOR * height * (SIGNLE_CHAR_WIDTH / SIGNLE_CHAR_HEIGHT))), Image.NEAREST)
width, height = im.size
print(width, height)
pix = im.load()

# Creates a PNG image with the ASCII, and with the background specified.
ASCII_image = Image.new("RGB", (SIGNLE_CHAR_WIDTH * width, SIGNLE_CHAR_HEIGHT * height), color = (0, 0, 0))
n = ImageDraw.Draw(ASCII_image)

# Creates a .txt file with the ASCII Artwork.
#text_file_with_ASCII = open("ASCII_Artwork.txt", "w")    <-------- Enable for text file.

# Character array logic & density:
char_array = list(chars)
char_array_length = len(char_array)
interval_of_density = char_array_length / MAX_RGB_VALUE

#---------------------------------------------------------------------------------------------------------------------------------------
# Brief : The <<grey>> RGB value is judged and assigned a character according to the specified <<chars>> array.
# Parameter character_input : The grey RGB integer.
# Return : Overwrites <<char_array>> to become an actual array, and assigns <<character_input>> a character from <<chars>>.
def getChar(character_input):

    return char_array[math.floor(character_input * interval_of_density)]

#---------------------------------------------------------------------------------------------------------------------------------------

# Checks through the whole image to determine the RGB values of one pixel at a time.
for i in range(height): # Row by row.
    for j in range(width): # Column by column.
        r, g, b = pix[j, i]

        # Takes the average RGB of a single pixel and creates a black & white alternative.
        grey = int((r + g + b) / 3)
        pix[j, i] = (grey, grey, grey)

        # Draws on the PNG file:
        n.text((j * SIGNLE_CHAR_WIDTH, i * SIGNLE_CHAR_HEIGHT), getChar(grey), font = font, fill = (r, g, b))

        # Writes on the text file.
        #text_file_with_ASCII.write(getChar(grey))    <-------- Enable for text file.
    
    #text_file_with_ASCII.write("\n")                 <-------- Enable for text file.

# Saves the new image:
ASCII_image.save("ASCII_Artwork.png")