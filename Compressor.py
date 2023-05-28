from PIL import Image

import os

download_folder = "C:/Users/David Daza/Downloads/"
images_folder = "C:/Users/David Daza/Pictures/Fondos/"
audio_folder = ""


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
