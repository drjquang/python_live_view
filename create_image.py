""""
    Date: Tue, 21/05/2024
    Desc: Create a square-text for winning number
    Info: size 64x64, png format
          using number formatted as integer
"""
from PIL import Image, ImageDraw, ImageFont
import random

COLOR_WHITE = '#FFFFFF'
COLOR_RED = '#FF6347'    # Actually, this is tomato color
COLOR_BLACK = '#36454F'  # Charcoal
COLOR_GREEN = '#0EF043'  # New leaf
COLOR_BLUE = '#oEF0EC'   # Emerald color for unknown number

GREEN_NUMBER = [0]
RED_NUMBERS = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
BLACK_NUMBERS = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]


def color_selector(number):
    if number in GREEN_NUMBER:
        return COLOR_GREEN
    elif number in RED_NUMBERS:
        return COLOR_RED
    elif number in BLACK_NUMBERS:
        return COLOR_BLACK
    else:
        return COLOR_BLUE


def icon_generate(number):
    # Create the square with background color
    color = color_selector(number)
    image = Image.new("RGB", (64, 64), color)
    draw = ImageDraw.Draw(image)
    # Create the text in the middle of the square
    text = str(number)
    font_size = 36
    font_type = "arialbd.ttf"
    font = ImageFont.truetype(font_type, font_size)
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:4]  # Get the text dimension
    height_offset = 3  # Make sure it stay in the middle, this is configured manually
    text_position = ((64 - text_width) // 2, (64 - text_height) // 2 - height_offset)
    draw.text(text_position, text, fill=COLOR_WHITE, font=font)
    return image


def random_generate_number():
    number = random.randint(0, 36)
    icon = icon_generate(number)
    icon.show()


def generate_all_numbers():
    for i in range(37):
        icon = icon_generate(i)
        icon.save(f"number_icon/{i}.png")  # Save the image
        icon.close()


if __name__ == "__main__":
    # random_generate_number()
    # generate_all_numbers()  # Already created, used once only
    pass
