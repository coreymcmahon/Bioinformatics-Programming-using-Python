def some(coll, pred=labmda x: x):
    """Return True if pred(item) is true for some item in coll"""
    return next((True for item in coll if pred(item)), False)
