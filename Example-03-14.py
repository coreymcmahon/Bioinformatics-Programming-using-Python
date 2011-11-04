def read_FASTA(filename):
    with open(filename) as file:
        return [(part[0].split('|')), part[2].replace('\n','')) for part in [entry.partition('\n') for entry in file.read().split('>')[1:]]]
