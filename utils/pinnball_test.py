DEFAULT_TEST_DATA = {
    1: [1, 4, 7],
    2: [1, 5, 3],
    3: [2, 2, 8],
    4: [1, 4, 7],
    5: [3, 4, 5],
    6: [8, 9, 9],
    7: [0, 0, 0],
    8: [2, 4, 7],
}


def pinball_test(test_data: dict, holes: int = 10) -> set:
    """ Checks results from multiple runs on pinball machine to validate all results are possible

    :param test_data: dict with keys as test number and values as list of results from that test
    :param holes: int number of holes/poles that machines has
    :return: set containing options that were never hit
    """
    result = set(range(holes))
    for data in test_data.values():
        result.difference_update(set(data))
    return result
