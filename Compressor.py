from PIL import Image

import os

download_folder = "C:/Users/David Daza/Downloads/"
images_folder = "C:/Users/David Daza/Pictures/Fondos/"
desk = "C:/Users/Public/Desktop/"


if __name__ == "__main__":
    for file_name in os.listdir(download_folder):
        name, extension = os.path.splitext(download_folder + file_name)

        if extension in [".jpg", ".png", ".jpeg"]:
            image = Image.open(download_folder + file_name)
            image.save(images_folder + "compressed_" + file_name, optimize=True, quality=50)
            os.remove(download_folder + file_name)
            print(name + ":" + extension)

        if extension in [".exe", ".msi"]:
            os.remove(download_folder + file_name)

if __name__ == "__main__":
    for file_desk in os.listdir(desk):
        name, extension = os.path.splitext(desk + file_desk)

        if extension in [".lnk"]:
            os.remove(desk + file_desk)