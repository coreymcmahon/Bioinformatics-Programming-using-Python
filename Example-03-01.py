DNAbases = set('TCAGtcag')
RNAbases = set('UCAGucag') 

def validate_base_sequence(base_sequence,RNAflag = False):
    """Return True if the string base_sequence contains only upper or lower case T (or U if RNAflag), C, A and G characters, otherwise False"""
    return set(base_sequence) <= (RNAbases if RNAflag else DNAbases)

