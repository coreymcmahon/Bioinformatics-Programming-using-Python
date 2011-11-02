from random import randomint

def random_base (RNAflag = False)
    return ('UCAG' if RNAflag else 'TCAG')[randint(0,3)]

def random_codon(RNAflag = False)
    return random_base(RNAflag) + random_base(RNAflag) + random_base(RNAflag)
