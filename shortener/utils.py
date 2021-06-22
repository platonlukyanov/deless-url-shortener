import random
import string
from PIL import Image
import io
from typing import Callable, Iterable


def image_to_byte_array(image: Image, format: str = "PNG") -> bytes:
    """Transforms PIL object to byte array"""
    img_bytea_array = io.BytesIO()
    image.save(img_bytea_array, format=format)
    img_bytea_array = img_bytea_array.getvalue()
    return img_bytea_array


def generate_code(length: int = 4) -> str:
    """Generates random ASCII code"""
    ascii_letters_list = list(string.ascii_letters)
    random.shuffle(ascii_letters_list)
    if length > len(ascii_letters_list):
        ascii_letters_list = ascii_letters_list * (length // len(ascii_letters_list))
    return "".join(ascii_letters_list[:length])


def get_unique_code(generate_function: Callable[..., str], previous_set: Iterable, start_length: int = 1) -> str:
    """Generating unique in previous set string, generate_function is required to have length  argument"""
    length = start_length
    while True:
        # try to generate unique code
        code = generate_function(length=length)
        if not (code in previous_set):
            return code
        length += 1

