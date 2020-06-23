def calculate_gradient(coord1, coord2):
    dy = coord2[1] - coord1[1]
    dx = coord2[0] - coord1[0]

    if dy == 0 or dx == 0:
        return 0
    else:
        return dy / dx
