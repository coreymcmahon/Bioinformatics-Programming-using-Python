# Example 3-6
def read_FASTA_strings(filename):
    with open(filename) as file:
        return file.read().split('>')[1:]

# Example 3-10
def read_FASTA_entries(filename):
    return [seq.partition('\n') for seq in read_FASTA_strings(filename)]

# Example 3-12
def read_FASTA_sequences(filename):
    return [(info[1:], seq.replace('\n', '')) for info, ignore, seq in read_FASTA_entries(filename)]

# Example 3-13
def read_FASTA_sequences_and_info(filename):
    return [[seq[0].split('|'), seq[1]] for seq in read_FASTA_sequences(filename)]


