from random import randint

def replace_base_randomly_using_names(base_seq):
    """Return a sequence with the base at a randomly selected position of base_seq replaced 
    by a base chosen randomly from the three bases that are not at that position"""
    position = randint(0, len(base_seq) - 1)    # -1 because len is one past end
    
    base = base_seq[position]
    bases = 'TCAG'
    bases.replace(base, '')    # replace with empty string 
    newbase = bases[randint(0,2)]
    beginning = base_seq[0:position]    # up to position
    end = base_seq[position+1:]    # omitting the base at position
    return beginning + newbase + end
