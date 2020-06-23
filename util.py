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
