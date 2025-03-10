import cv2
import numpy as np

def apply_style_transfer(content_image, style_image, alpha=0.7):
    """Blends style image into content image using color transfer."""
    content_lab = cv2.cvtColor(content_image, cv2.COLOR_RGB2LAB)
    style_lab = cv2.cvtColor(style_image, cv2.COLOR_RGB2LAB)

    l_content, a_content, b_content = cv2.split(content_lab)
    l_style, a_style, b_style = cv2.split(style_lab)

    l_result = cv2.addWeighted(l_content, alpha, l_style, 1 - alpha, 0)
    a_result = cv2.addWeighted(a_content, alpha, a_style, 1 - alpha, 0)
    b_result = cv2.addWeighted(b_content, alpha, b_style, 1 - alpha, 0)

    result = cv2.merge((l_result, a_result, b_result))
    return cv2.cvtColor(result, cv2.COLOR_LAB2RGB)
