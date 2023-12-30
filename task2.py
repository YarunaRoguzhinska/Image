from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('mops.jpeg') as  pic_original:
    box = (100,100,400,450)
    cropped = pic_original.crop(box)
    cropped.save("size.jpg")