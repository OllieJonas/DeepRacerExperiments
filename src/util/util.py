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


