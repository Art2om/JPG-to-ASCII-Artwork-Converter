import os
import cv2
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
        
        frames_turned_into_ASCII = 0
        for image_file in os.listdir(frame_folder_path):
            frame_converter = Converter_for_Image(f"{frame_folder_path}/{image_file}")
            ASCII_string_of_frame = frame_converter.convert_image_to_ASCII_through_average()
            ASCII_image_of_frame = frame_converter.draw_ASCII_image(ASCII_string_of_frame)
            ASCII_image_of_frame.save(f"{non_existant_ASCII_frames_folder}/frame_{frames_turned_into_ASCII}.png")
            del frame_converter
            frames_turned_into_ASCII += 1

        