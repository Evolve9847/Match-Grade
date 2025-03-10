import cv2
import numpy as np
from flask import request
import os

def load_image(image_path):
    """Load an image from a given path."""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error loading image: {image_path}")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def save_image(image, output_path):
    """Save an image to the given output path."""
    cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
