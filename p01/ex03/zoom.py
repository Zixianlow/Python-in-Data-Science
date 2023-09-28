from load_image import ft_load
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def ft_zoom():
    """Load image using ft_load and crop the image to have size of (x,y,1).
Then, squeeze it to a (x,y) shape. Get the image using Image.fromarray and
stores it into im. Prints out the new shape and the array. Make a blank
image and draw axes and interval to the blank image then paste the new image
into it. Show the end"""
    print("The shape of image is:", end=" ")
    image_array = ft_load("animal.jpeg")
    print(image_array)
    cropped_image_chn0 = image_array[96:496, 440:840, :]
    cropped_image = np.mean(cropped_image_chn0, axis=2,
                            keepdims=True).astype(np.uint8)
    cropped_image_2d = np.squeeze(cropped_image)
    im = Image.fromarray(cropped_image_2d)
    print("New shape after slicing:", end=" ")
    print(cropped_image.shape, "or", cropped_image_2d.shape)
    print(cropped_image)
    width, height = 450, 450
    image = Image.new("RGB", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.line([(25, height - 25), (425, height - 25)], fill="black", width=2)
    draw.line([(25, 425), (25, 25)], fill="black", width=2)
    font = ImageFont.load_default()
    for i in range(75, 426, 50):
        draw.text((5, height - i - 5), str(425 - i), fill="black", font=font)
        draw.line([(20, height - i), (25, height - i)], fill="black", width=2)
    for i in range(25, 401, 50):
        draw.text((i, height - 15), str(i - 25), fill="black", font=font)
        draw.line([(i, height - 20), (i, height - 25)], fill="black", width=2)
    image.paste(im, (25, 25))
    image.show()


if __name__ == "__main__":
    ft_zoom()
