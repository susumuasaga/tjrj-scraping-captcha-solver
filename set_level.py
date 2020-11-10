import numpy as np


def set_white_level(img: np.ndarray, threshold):
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            value = img[i, j]
            if value >= threshold:
                value = 255
            img[i, j] = value


def set_black_level(img: np.ndarray, threshold):
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            value = img[i, j]
            if value <= threshold:
                value = 0
            img[i, j] = value
