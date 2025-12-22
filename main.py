from converter import Converter

image_path = "Andromeda_Galaxy.jpeg"
converter = Converter(image_path)
image = converter.scaled_image()
image.save("result.png")