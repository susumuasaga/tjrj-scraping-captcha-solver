import numpy as np
from scipy.interpolate import RectBivariateSpline

from set_level import set_white_level


def get_r0(img: np.ndarray):
    j = img.shape[1] - 1
    while (
        img[31, j] > 0
        or img[29, j] > 0
        or img[31, j - 1] > 0
        or img[29, j - 1] > 0
    ):
        j -= 1
    return j - 109


def get_white_level(img: np.ndarray):
    return min(img[1, 1], img[1, -2], img[-2, 1], img[-2, -2])


xs = np.genfromtxt("xs.csv")
ys = np.linspace(-24.0, 24.0, 9) / 63
xds = np.genfromtxt("xds.csv", delimiter=",")
yds = np.genfromtxt("yds.csv", delimiter=",")
f = RectBivariateSpline(xs, ys, xds)
g = RectBivariateSpline(xs, ys, yds)


def distort(xu, yu):
    sqr_r = xu ** 2 + yu ** 2
    if sqr_r < 1:
        return f(xu, yu)[0, 0], g(xu, yu)[0, 0]
    else:
        return xu, yu


def to_row_col(x, y, r0=63, row0=30, col0=110):
    return y * r0 + row0, x * r0 + col0


def to_x_y(row, col, r0=63, row0=30, col0=110):
    return (col - col0) / r0, (row - row0) / r0


def undistort(image):
    image[-1, :] = 255
    set_white_level(image, get_white_level(image))
    r0 = get_r0(image)
    h, w = image.shape
    img_function = RectBivariateSpline(
        np.arange(h), np.arange(w), image, kx=1, ky=1
    )
    result = np.full(image.shape, 255, dtype="uint8")
    for row in range(13, 54):
        for col in range(13, 162):
            row_d, col_d = to_row_col(*distort(*to_x_y(row, col, r0=r0)), r0=r0)
            if 0 <= row_d <= h - 1 and 0 <= col_d <= w - 1:
                result[row, col] = int(img_function(row_d, col_d)[0, 0] + 0.5)
    return result
