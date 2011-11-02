def validate_base_sequence(base_sequence, RNAflag = False):
    """Return True if the string base_sequence contains only upper or lower case T (or U if RNAflag), C, A and G characters, otherwise False """
    seq = base_sequence.upper()
    return len(seq) == (seq.count('U' if RNAflag else 'T') + seq.count('C') + seq.count('A') + seq.count('G'))

def gc_content(base_seq):
    """Return the percentage of bases in base_seq that are C or G"""
    assert validate_base_sequence(base_seq), \
        'argument has invalid characters'
    seq = base_seq.upper()
    return (base_seq.count('G') + base_seq.count('C')) / len(base_seq)

def recognition_site(base_seq, recognition_seq):
    """Return the first position in the base_seq where recognition_seq occurs or -1 if not found"""
    return base_seq.find(recognition_seq)

def test():
    assert validate_base_sequence('ACTG')
    assert validate_base_sequence('')
    assert not validate_base_sequence('ACUG')

    assert validate_base_sequence('ACUG', False)
    assert not validate_base_sequence('ACUG', True)
    assert validate_base_sequence('ACTG', True)

    assert .5 == gc_content('ACTG')
    assert 1.0 == gc_content('CCGG')
    assert .25 == gc_content('ACTT')

    print('All tests passed.')

test()
