from PIL import Image
from PIL import ImageFilter

with Image.open('photo1.jpg') as  pic_original:
    print("розмір: ", pic_original.size)
    print("формат: ", pic_original.format)
    print("тип: ", pic_original.mode)
    #pic_original.show()
    photo1_gray = pic_original.convert('L')
    photo1_gray.save('photo1gray.jpg')
    photo1_blured = pic_original.filter (ImageFilter.BLUR)
    ph1_up = pic_original.transpose(Image.ROTATE_180)
    photo1_blured.save('ph1blur.jpg')
    ph1_up.save('rotate.jpg')