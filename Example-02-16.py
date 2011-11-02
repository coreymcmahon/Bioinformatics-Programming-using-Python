from random import randint

def replace_base_randomly_using_expression(base_seq):
    position = randint(0, len(base_seq) - 1)
    return (base_seq[0:position] + 'TCAG'.replace(base_seq[position], '')[randint(0,2)] + base_seq[position+1:])
