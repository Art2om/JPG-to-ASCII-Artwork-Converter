import os
import cv2
from PIL import Image
from converter_for_Image import Converter_for_Image

class Converter_for_Video:
    def __init__(self, video_path:str):
        self.video = cv2.VideoCapture(video_path)
    
    def __del__(self):
        self.video.release()
        print("Converter_for_Video instance closed.")
    
    def get_all_frames_from_video(self, non_existant_frame_folder_path:str):
        frame_number = 0
        state = True
        
        if (not os.path.exists(non_existant_frame_folder_path)):
            os.mkdir(non_existant_frame_folder_path)
        else:
            print(f"Directory {non_existant_frame_folder_path} already exists.")
            return

        while (state == True):
            state, frame = self.video.read()
            if (state == True):
                cv2.imwrite(f"{non_existant_frame_folder_path}/frame_{frame_number}.png", frame)
                frame_number += 1
        print(f"Number of frames saved: {frame_number}")
    
    def turn_all_images_into_ASCII_inside_folder(self, frame_folder_path:str, non_existant_ASCII_frames_folder:str):
        if (not os.path.exists(frame_folder_path)):
            print("The frame folder does not exist.")
            return
        
        if (not os.path.exists(non_existant_ASCII_frames_folder)):
            os.mkdir(non_existant_ASCII_frames_folder)
        else:
            print(f"Directory {non_existant_ASCII_frames_folder} already exists.")
            return
        
        frame_name_paths = os.listdir(frame_folder_path)
        frame_name_paths.sort(key = lambda file_name: int(file_name.split("_")[1].split(".")[0]))
        #print(frame_name_paths)

        frames_turned_into_ASCII = 0
        for image_file in frame_name_paths:
            frame_converter = Converter_for_Image(f"{frame_folder_path}/{image_file}")
            ASCII_string_of_frame = frame_converter.convert_image_to_ASCII_through_average()
            ASCII_image_of_frame = frame_converter.draw_ASCII_image(ASCII_string_of_frame)
            ASCII_image_of_frame.save(f"{non_existant_ASCII_frames_folder}/frame_{frames_turned_into_ASCII}.png")
            del frame_converter
            frames_turned_into_ASCII += 1
        print(f"Total images turned into ASCII: {frames_turned_into_ASCII}")
    
    def make_video_from_ASCII_folder(self, frame_folder_path:str):
        ASCII_image = Image.open(f"{frame_folder_path}/frame_0.png")
        image_width = ASCII_image.width
        image_height = ASCII_image.height
        ASCII_image.close()

        video_writer = cv2.VideoWriter(filename = "product.mp4",
                                        fourcc = cv2.VideoWriter_fourcc(*'mp4v'),
                                        fps = self.video.get(cv2.CAP_PROP_FPS),
                                        frameSize = (image_width, image_height))
        
        image_name_paths = os.listdir(frame_folder_path)
        image_name_paths.sort(key = lambda file_name: int(file_name.split("_")[1].split(".")[0]))
        #print(image_name_paths)

        for image_path in image_name_paths:
            image = cv2.imread(f"{frame_folder_path}/{str(image_path)}")
            video_writer.write(image)

        video_writer.release()

        