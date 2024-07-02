from PIL import Image
import os

path = "C:\\Users\\asus\\Downloads\\Posture.v2-good-posture.yolov8\\test\\images"   #file name should be a word

def resize(width, height):
    # List all files in the specified directory
    dirs = os.listdir(path)
    
    for item in dirs:
        file_path = os.path.join(path, item)
        
        if os.path.isfile(file_path):
            img = Image.open(file_path)
            new_image = img.resize((width, height))
            new_file_name = 'resized-' + item
            new_file_path = os.path.join(path, new_file_name)
            new_image.save(new_file_path)
            print(f"Resized image saved as {new_file_path}")

resize(640, 640)
