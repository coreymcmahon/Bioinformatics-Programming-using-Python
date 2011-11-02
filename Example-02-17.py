from random import randint

def replace_base_randomly(base_seq):
    position = randint(0, len(base_seq) - 1)
    bases = 'TCAG'.replace(base_seq[position], '')
    return (base_seq[0:position] + bases[randint(0,2)] + base_seq[position+1:])
