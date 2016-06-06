def get_index(trades, x):
    """ Locate the leftmost value greater or equal to x in a list of trades"""
    hi = len(trades)
    lo = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if trades[mid].trade_time < x:
            lo = mid + 1
        else:
            hi = mid

    if lo != len(trades) and trades[lo].trade_time >= x:
        return lo
    raise ValueError
