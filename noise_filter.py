import numpy as np
import cv2

from set_level import set_white_level, set_black_level


def clean_center_row(image: np.ndarray):
    for col in range(image.shape[1]):
        if image[28, col] > image[29, col]:
            image[29, col] = image[28, col]
        if image[32, col] > image[31, col]:
            image[31, col] = image[32, col]
        image[30, col] = (int(image[29, col]) + int(image[31, col])) // 2


def redraw(image: np.ndarray, brush: np.ndarray):
    h, w = image.shape
    brush_h, brush_w = brush.shape
    anchor_y = brush_h // 2
    anchor_x = brush_w // 2
    result = np.full((h, w), 255, dtype="uint8")
    for row in range(h):
        for col in range(w):
            if image[row, col] == 0:
                for i in range(brush_h):
                    for j in range(brush_w):
                        result[row + i - anchor_y, col + j - anchor_x] &= brush[
                            i, j
                        ]
    return result


kernel = np.ones((3, 3)) / 9
brush = np.zeros((3, 3), dtype="uint8")


def clean(image: np.ndarray, threshold=30):
    result = np.copy(image)
    clean_center_row(result)
    result = cv2.filter2D(result, -1, kernel)
    set_white_level(result, threshold)
    set_black_level(result, threshold - 1)
    result = redraw(result, brush)
    return result
