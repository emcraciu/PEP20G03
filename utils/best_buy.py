DEFAULT_SHOPS = (
    {'lego': 50, 'HotWheels': 60, 'Barbie': 30, "toy1": 30},
    {'lego': 60, 'HotWheels': 55, 'Barbie': 25, "toy2": 31},
    {'lego': 55, 'HotWheels': 70, 'Barbie': 14, "toy3": 32}
)


def best_buy(*args: dict, to_buy: dict = None) -> int:
    """Function to calculate best price in shop
    :param args: dict with shop items
    :param to_buy: list with shopping information
    :return: int best price of all shops
    """
    best_price = None
    for shop in args:
        shop_total = 0
        for item_name, pieces in to_buy.items():
            shop_total += pieces * shop[item_name]
        if not best_price or best_price > shop_total:
            best_price = shop_total
    return best_price
