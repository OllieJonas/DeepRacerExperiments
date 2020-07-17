import numpy as np


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


def pretty_print(d, indent=0):
    """
    Pretty prints a dictionary.

    :param d:
    :param indent:
    :return:
    """
    for key, value in d.items():
        print('\t' * indent + str(key) + ":")
        if isinstance(value, dict):
            pretty_print(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


def circle_metrics(coord1, coord2, coord3, debug=False):
    """
    Gives metrics about a circle (radius, equation, etc.) based on 3 given points.

    Calculated from here: http://ambrsoft.com/TrigoCalc/Circle3D.htm
    :param coord1:
    :param coord2:
    :param coord3:
    :param debug:
    :return:
    """
    x1, y1 = [a for a in coord1]
    x2, y2 = [a for a in coord2]
    x3, y3 = [a for a in coord3]

    x1_sqr, x2_sqr, x3_sqr = pow(x1, 2), pow(x2, 2), pow(x3, 2)
    y1_sqr, y2_sqr, y3_sqr = pow(y1, 2), pow(y2, 2), pow(y3, 2)

    det_a = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
    det_b = (x1_sqr + y1_sqr) * (y3 - y2) + (x2_sqr + y2_sqr) * (y1 - y3) + (x3_sqr + y3_sqr) * (y2 - y1)
    det_c = (x1_sqr + y1_sqr) * (x2 - x3) + (x2_sqr + y2_sqr) * (x3 - x1) + (x3_sqr + y3_sqr) * (x1 - x2)
    det_d = (x1_sqr + y1_sqr) * ((x3 * y2) - (x2 * y3)) + (x2_sqr + y2_sqr) * ((x1 * y3) - (x3 * y1)) + (x3_sqr + y3_sqr) * ((x2 * y1) - (x1 * y2))

    if debug:
        print("A Det: {}. B Det: {}. C Det: {}. D Det: {}".format(det_a, det_b, det_c, det_d))

    if det_a == 0:
        centre_x, centre_y = None, None
        radius = np.Inf
    else:
        centre_x, centre_y = -1 * (det_b / (2 * det_a)), -1 * (det_c / (2 * det_a))
        radius = np.sqrt((det_b ** 2 + det_c ** 2 - 4 * det_a * det_d) / (4 * det_a ** 2))

    return {
        "coords": [coord1, coord2, coord3],
        "centre": (centre_x, centre_y),
        "radius": radius
    }


if __name__ == "__main__":
    circle_metrics([1, 3], [2, 7], [3, 5], True)
