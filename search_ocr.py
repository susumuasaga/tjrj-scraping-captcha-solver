import numpy as np

from noise_filter import clean
from ocr import read


def read(image: np.ndarray):
    best_confidence = 0
    best_image = np.array([])
    best_text = ""
    best_threshold = 0
    for threshold in range(17, 31):
        filtered = clean(image, threshold)
        text, confidence = read(filtered)
        if len(text) == 7 and confidence > best_confidence:
            best_image = filtered
            best_confidence = confidence
            best_text = text
            best_threshold = threshold
    return best_text, best_image, best_confidence, best_threshold
