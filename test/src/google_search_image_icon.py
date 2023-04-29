# create function read List of image name from file and create new image with new name and save to output folder

import os
from PIL import Image

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read().splitlines()
    
def create_image_from_list(file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    img = Image.open(file_path)
    names = read_file("list_image_name.txt")
    for i, name in enumerate(names):
        new_name = f"{name}.png"
        output_path = os.path.join(output_dir, new_name)
        img_copy = img.copy()
        img_copy.save(output_path)
        print(f"Đã lưu ảnh {i+1}/{len(names)}: {new_name}")


if __name__ == "__main__":
    img_path = "../media/google_image_search.png"
    output_dir = "../../media/"
    create_image_from_list(img_path, output_dir)