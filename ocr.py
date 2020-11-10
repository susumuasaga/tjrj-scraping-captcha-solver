import os
from numbers import Number

import pytesseract
import numpy as np

os.environ["TESSDATA_PREFIX"] = "./tessdata/"


def read(image):
    data = pytesseract.image_to_data(
        image,
        config="--psm 8 captcha",
        output_type=pytesseract.Output.DICT,
    )
    text = data["text"]
    confidences = []
    num_chars = []
    result = ""

    for i in range(len(text)):
        if isinstance(data["conf"][i], Number):
            confidences.append(data["conf"][i])
            num_chars.append(len(text[i]))
            result += text[i]
    if np.sum(num_chars) == 0:
        confidence = 0
    else:
        confidence = np.average(confidences, weights=num_chars)
    return result, confidence
