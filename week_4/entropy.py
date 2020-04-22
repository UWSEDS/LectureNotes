import numpy as np
# Code Under Test
def entropy(ps):
    if any([(p < 0.0) or (p > 1.0) for p in ps]):
        raise ValueError("Bad input.")
    if sum(ps) > 1:
        raise ValueError("Bad input.")
    items = ps * np.log(ps)
    new_items = []
    for item in items:
        if np.isnan(item):
            new_items.append(0)
        else:
            new_items.append(item)
    return np.abs(-np.sum(new_items))
