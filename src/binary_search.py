""" A module for finding the index of the first trades recorded within 15 minutes of the current time"""


def valid(x, y):
    """ Check x>=y."""
    return x >= y


def get_index_binary_search(trades, x):
    """ Locate the leftmost value greater or equal to x in a list of trades"""

    if not trades:
        return -1

    if valid(trades[0].trade_time, x):
        return 0

    if not valid(trades[-1].trade_time, x):
        return -1

    high = len(trades)
    low = 0

    while low < high:
        mid = (low + high) / 2
        if valid(trades[mid].trade_time, x):
            if not valid(trades[mid - 1].trade_time, x):
                return mid
            else:
                high = mid
        else:
            if valid(trades[mid + 1].trade_time, x):
                return mid + 1
            else:
                low = mid