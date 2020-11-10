import cv2

import noise_filter
import ocr
from captcha_distortion import undistort


def test_327gv25():
    image = cv2.imread("./data/captcha_327gv25.png", cv2.IMREAD_GRAYSCALE)
    captcha, _ = ocr.read(noise_filter.clean(undistort(image)))
    assert captcha == "327gv25"


def test_fn7tasd():
    image = cv2.imread("./data/captcha_fn7tasd.png", cv2.IMREAD_GRAYSCALE)
    captcha, _ = ocr.read(noise_filter.clean(undistort(image)))
    assert captcha == "fn7tasd"


def test_ssp86p0():
    image = cv2.imread("./data/captcha_ssp86p0.png", cv2.IMREAD_GRAYSCALE)
    captcha, _ = ocr.read(noise_filter.clean(undistort(image)))
    assert captcha == "ssp86p0"
