import numpy as np

def entropy(ps):
    check1 = (0 <= sum(ps)) and (1 >= sum(ps))
    trues = [(0 <= v) and (1 >= v) for v in ps]
    if not( check1 and all(trues)):
        raise ValueError("Invalid input.")
    return -sum(ps * np.log(ps))
