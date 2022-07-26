#Use the pillow library to load a colorful image from your computer and 
# convert it into a grayscale image

from PIL import Image

def get_gray(file_path):
    with Image.open(file_path) as im:
        im.show()
        im_gray = im.convert("L")
        im_gray.show()

    #im_gray.save(file_path)        to save image to comp, prob don't put in func

picture = get_gray("bobsburgers.jpg")