# OSError: cannot write mode RGBA as JPEG Pillow error

from PIL import Image

with Image.open("house.png") as im:

    if im.mode in ('RGBA', 'P'):
        rgb_im = im.convert('RGB')

        rgb_im.save('house.jpg')
    elif im.mode in ('RGB', 'JPEG'):
        im.save('house123.jpg')