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

    return pow(dx_squared + dy_squared, 1/2)


def circle_metrics(coord1, coord2, coord3):
    """
    Gives metrics about a circle (radius, equation, etc.) based on 3 given points.

    Calculated from here: http://ambrsoft.com/TrigoCalc/Circle3D.htm
    :param coord1:
    :param coord2:
    :param coord3:
    :return:
    """
    x1, y1 = [x for x in coord1]
    x2, y2 = [x for x in coord2]
    x3, y3 = [x for x in coord3]


    pass


if __name__ == "__main__":
    radius_of_circle([1, 3], [2, 7], [3, 5])
