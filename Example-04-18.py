def extract_matching_sequences(filename, string):
    """From a FASTA file named filename, extract all sequences whose descriptions contain string"""
    sequences = []
    seq = ''
    with open(filename) as file:
        for line in file:
            if line[0] == '>':  # Is this the first line of the sequence? Is this the metadata?
                if seq:
                    sequences.append(seq)
                seq = ''
                includeflag = string in line # does the line contain the str in 'string'?
            else:
                if includeflag: # if the value IS in the description, include the sequence data
                    seq += line[:-1]
        if seq:
            sequences.append(seq)
    return sequences
