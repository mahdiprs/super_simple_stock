""" A module for finding the index of the first trades recorded within 15 minutes of the current time"""


def valid(x, y):
    """ Check x>=y."""
    return x >= y


def get_index_binary_search(trades, value):
    """ Locate the leftmost value greater or equal to x in a list of trades"""

    if not trades:
        raise IndexError

    if valid(trades[0].trade_time, value):
        return 0

    if not valid(trades[-1].trade_time, value):
        raise IndexError

    high = len(trades)
    low = 0

    while low < high:
        mid = (low + high) / 2
        if valid(trades[mid].trade_time, value):
            if not valid(trades[mid - 1].trade_time, value):
                return mid
            else:
                high = mid
        else:
            if valid(trades[mid + 1].trade_time, value):
                return mid + 1
            else:
                low = mid
