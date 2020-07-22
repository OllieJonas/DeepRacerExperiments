import math


def calculate_gradient(coord1, coord2):
    """
    Calculates the gradient between two given coordinates.

    :param coord1: The first coordinate
    :param coord2: The second coordinate
    :return: The gradient between the two
    """
    dy = coord2[1] - coord1[1]
    dx = coord2[0] - coord1[0]

    if dx == 0:  # Cannot divide by 0, therefore assume is 0
        return 0

    return dy / dx


def distance_between(coord1, coord2):
    """
    Calculates the distance between two given coordinates

    :param coord1: The first coordinate
    :param coord2: The second coordinate
    :return: The distance between the two
    """
    dx = coord2[0] - coord1[0]
    dy = coord2[1] - coord1[1]

    dx_squared = pow(dx, 2)
    dy_squared = pow(dy, 2)

    return pow(dx_squared + dy_squared, 1 / 2)


def take_closest(entries, n):
    """
    Assumes entries is sorted. Returns closest value to n.

    If two numbers are equally close, return the smallest number.
    """
    from bisect import bisect_left

    pos = bisect_left(entries, n)
    if pos == 0:
        return entries[0]
    if pos == len(entries):
        return entries[-1]
    before = entries[pos - 1]
    after = entries[pos]
    if after - n < n - before:
        return after
    else:
        return before


def calculate_circle_metrics(coord1, coord2, coord3, debug=False):
    # Calculated from here: http://ambrsoft.com/TrigoCalc/Circle3D.htm
    x1, y1 = [a for a in coord1]
    x2, y2 = [a for a in coord2]
    x3, y3 = [a for a in coord3]

    x1_sqr, x2_sqr, x3_sqr = pow(x1, 2), pow(x2, 2), pow(x3, 2)
    y1_sqr, y2_sqr, y3_sqr = pow(y1, 2), pow(y2, 2), pow(y3, 2)

    det_a = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
    det_b = (x1_sqr + y1_sqr) * (y3 - y2) + (x2_sqr + y2_sqr) * (y1 - y3) + (x3_sqr + y3_sqr) * (y2 - y1)
    det_c = (x1_sqr + y1_sqr) * (x2 - x3) + (x2_sqr + y2_sqr) * (x3 - x1) + (x3_sqr + y3_sqr) * (x1 - x2)
    det_d = (x1_sqr + y1_sqr) * ((x3 * y2) - (x2 * y3)) + (x2_sqr + y2_sqr) * ((x1 * y3) - (x3 * y1)) + (
            x3_sqr + y3_sqr) * ((x2 * y1) - (x1 * y2))

    if debug:
        print("A Det: {}. B Det: {}. C Det: {}. D Det: {}".format(det_a, det_b, det_c, det_d))

    if det_a == 0:
        centre_x, centre_y = None, None
        radius = math.inf
    else:
        centre_x, centre_y = -1 * (det_b / (2 * det_a)), -1 * (det_c / (2 * det_a))
        radius = math.sqrt((det_b ** 2 + det_c ** 2 - 4 * det_a * det_d) / (4 * det_a ** 2))

    return {
        "coords": [coord1, coord2, coord3],
        "centre": (centre_x, centre_y),
        "radius": radius
    }