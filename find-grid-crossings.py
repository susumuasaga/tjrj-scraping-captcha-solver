from typing import Tuple

import numpy as np


def img_sym_x(img: np.ndarray, y: int, x: int) -> int:
    w = img.shape[1]
    return img[y, x] | img[y, w - x]


def step_int(coord: float, incr: int) -> int:
    if coord.is_integer():
        return int(coord - 0.5 + 1.5 * incr)
    else:
        return int(coord - 0.5 + incr)


def next_intersection(
    img: np.ndarray, x: float, y: float, incr_x: int, incr_y: int
) -> Tuple[float, float]:
    x_int = step_int(x, incr_x) + incr_x
    while True:
        y = next_y(img, x_int, y - 2 * incr_y, incr_y)
        y4_int = step_int(y, incr_y)
        if img[y4_int, x_int] == 0:
            break
        x_int += incr_x
    # img[y4_int, x_int] == 0
    x1, y1 = x_int + 0.5, y
    # (x1, y1) in horizontal line before crossing
    assert (
        img_sym_x(img, y4_int, x_int) != 0
        and img_sym_x(img, y4_int, x_int + incr_x) != 0
    )
    x4, y4 = x_int + 0.5, y4_int + 0.5
    if img[y4_int, x_int + incr_x] == 0:
        x4 += 0.5 * incr_x
    # (x4, y4) in vertical line after crossing
    x_int += incr_x
    y = next_y(img, x_int, y - 2 * incr_y, incr_y)
    x2, y2 = x_int + 0.5, y
    # (x2, y2) in horizontal line after crossing
    y3_int = step_int(y, -incr_y)
    assert (
        img_sym_x(img, y3_int, x_int) != 0
        and img_sym_x(img, y3_int, x_int - incr_x) != 0
    )
    x3, y3 = x_int + 0.5, y3_int + 0.5
    if img[y3_int, x_int] == 0:
        if img[y3_int, x_int - incr_x] == 0:
            x3 -= 0.5 * incr_x
    else:
        assert img[y3_int, x_int - incr_x] == 0
        x3 -= incr_x
    # (x3, y3) in vertical line before crossing
    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    assert abs(det) > 0.01
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / det
    assert 0.0 <= t <= 1.0
    u = ((x1 - x2) * (y3 - y1) - (y1 - y2) * (x3 - x1)) / det
    assert 0.0 <= u <= 1.0
    xh, yh = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
    xv, yv = x3 + u * (x4 - x3), y3 + u * (y4 - y3)
    assert abs(xh - xv) < 0.01
    assert abs(yh - yv) < 0.01
    return (xh + xv) / 2, (yh + yv) / 2


def next_y(img: np.ndarray, x_int: int, y: float, incr_y: int) -> float:
    y_int = step_int(y, incr_y)
    while img_sym_x(img, y_int, x_int) != 0:
        y_int += incr_y
    # img_sym_x(img, y_int, x) == 0
    y = y_int + 0.5
    if img_sym_x(img, y_int + incr_y, x_int) == 0:
        y += 0.5 * incr_y
    return y


def find_horizontal_crossings(
    img: np.ndarray, m: int, y: float, incr_y: int
) -> np.ndarray:
    x_int = img.shape[1] // 2
    xl = xr = x_int + 0.5
    yl = yr = y
    row = np.zeros((m, 2))
    for j in range(m // 2, m):
        row[m - 1 - j] = xl, yl = next_intersection(
            img, xl, yl, -1, incr_y
        )
        row[j] = xr, yr = next_intersection(img, xr, yr, 1, incr_y)
    return row


def find_grid_crossings(
    img: np.ndarray, pattern_size: Tuple[int, int]
) -> np.ndarray:
    """
    Finds the positions of internal crossings of the grid.
    """
    n = pattern_size[0]
    m = pattern_size[1]
    matrix = np.zeros((n, m, 2), np.float32)
    xc_int = img.shape[1] // 2
    yu = yd = img.shape[0] / 2 + 0.5
    ic = (n - 1) // 2
    matrix[ic] = find_horizontal_crossings(img, m, yu, 1)
    for i in range(ic + 1, n):
        yu = next_y(img, xc_int, yu, -1)
        matrix[n - 1 - i] = find_horizontal_crossings(img, m, yu, -1)
        yd = next_y(img, xc_int, yd, 1)
        matrix[i] = find_horizontal_crossings(img, m, yd, 1)
    return matrix.reshape(-1, 2)
