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
