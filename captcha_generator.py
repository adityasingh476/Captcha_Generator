from captcha.image import ImageCaptcha
import string
import random
from PIL import Image
from io import BytesIO
import os

# Generate a random 8-character CAPTCHA text
n = 8
captcha_text = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))

# Create a CAPTCHA image
image = ImageCaptcha(width=400, height=200)
captcha_image = image.generate_image(captcha_text)

# Define the save path (use raw string or double backslashes for Windows paths)
save_path = r"C:\Users\265663\OneDrive\Documents\Aditya Singh\ID-1.jpeg"

# Save the image
captcha_image.save(save_path)

# Open and show the image
saved_image = Image.open(save_path)
saved_image.show()
