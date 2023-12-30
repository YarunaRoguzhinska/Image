from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('mops.jpeg') as  pic_original:

    pic_up = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_up.save('mirrow.jpg')

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('contr.jpg')