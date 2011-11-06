def read_FASTA_iteration(filename):
    sequences = []     # initialise...
    descr = None
    with open(filename) as file:     # Open the file...
        for line in file:
            if line[0] == '>':       # We've found the next entry 
                if descr:            # if we've already got a description in the buffer, we've found the end of the last entry
                    sequences.append((descr,seq)) # append it...
                descr = line[1:-1].split('|') # split up the description by 'pipe'
                seq = '' # reset the sequence buffer
            else:
                seq += line[:-1] # this ISN'T the start of the next entry, so feed the data into the sequence buffer
        sequences.append((descr,seq)) # This is for the last sequence in the file (as there will be no 'next sequence' character to prompt us to append it 
    return sequences

def read_FASTA(filename):
    with open(filename) as file:
        return [(part[0].split('|'), part[2].replace('\n','')) # Break the metadata into constituent parts (delimited by '|') and get rid of newline characters in the sequence data
                   for part in [entry.partition('\n')   # Split each item into 3 parts, the definition, a 'throw away' element (\n) and the sequence data. 
                       for entry in file.read().split('>')[1:] # Read the whole file and split on '>', ignoring the first item from the result of the split
                   ]
            ]

def read_FASTA_loop(filename):
    sequences = []
    descr = None
    with open(filename) as file:
        line = file.readline()[:-1]
        while line:
            if line[0] == '>':
                if descr:
                    sequences.append((descr, seq))
                descr = line[1:].split('|')
                seq = ''
            else:
                seq += line
            line = file.readline()[:-1]
        sequences.append((descr, seq))
    return sequences
