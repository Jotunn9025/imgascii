from PIL import Image
import numpy as np
img = Image.open('image.jpg')
new_width = 100
new_height = int(img.size[1] * (new_width / img.size[0]))
resized_img = img.resize((new_width, new_height))
gray_image = resized_img.convert('L')
img_array = np.asarray(gray_image)
ascii_chars = brightness_chars = '@%#X*+=-:. '
ascii_art = ''
for row in img_array:
    for brightness in row:
        ascii_art += ascii_chars[int(brightness / 255 * (len(ascii_chars) - 1))]
    ascii_art += '\n'
with open('image_ascii.txt', 'w') as f:
    f.write(ascii_art)
