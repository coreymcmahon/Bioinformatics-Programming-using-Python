def generate_triples(chars='TCAG'):
    """Return a list of all three-character combinations of unique characters in chars"""
    return [b1 + b2 + b3 for b1 in chars for b2 in chars for b3 in chars]
